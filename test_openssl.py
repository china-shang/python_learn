#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import OpenSSL
import time
import os
def get_crt(commonname):
    ca_validity_years = 10
    ca_validity = 24 * 60 * 60 * 365 * ca_validity_years

    certfile =  commonname + '.crt'
    if os.path.exists(certfile):
        print("find certfile")
        return certfile
    sans = ()
    with open("CA.crt", "rb") as f:
        context = f.read()
        key = OpenSSL.crypto.load_privatekey(
            OpenSSL.crypto.FILETYPE_PEM, context)
        ca = OpenSSL.crypto.load_certificate(
            OpenSSL.crypto.FILETYPE_PEM, context)

        pkey = OpenSSL.crypto.PKey()
        pkey.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)
        req = OpenSSL.crypto.X509Req()
        subj = req.get_subject()
        subj.countryName = 'CN'
        subj.stateOrProvinceName = 'Internet'
        subj.localityName = 'Cernet'
        subj.organizationalUnitName = ' Branch'
        if commonname[0] == '.':
            subj.commonName = '*' + commonname
            subj.organizationName = '*' + commonname
            sans = ['*' + commonname] + \
                [x for x in sans if x != '*' + commonname]
        else:
            subj.commonName = commonname
            subj.organizationName = commonname
            sans = [commonname] + [x for x in sans if x != commonname]
        #req.add_extensions([OpenSSL.crypto.X509Extension(b'subjectAltName', True, ', '.join('DNS: %s' % x for x in sans)).encode()])
        req.set_pubkey(pkey)
        ca_digest = "sha256"
        req.sign(pkey, ca_digest)

        cert = OpenSSL.crypto.X509()
        cert.set_version(2)
        cert.set_serial_number(int(time.time() * 1000))
        cert.gmtime_adj_notBefore(-600)  # avoid crt time error warning
        cert.gmtime_adj_notAfter(ca_validity)
        cert.set_issuer(ca.get_subject())
        cert.set_subject(req.get_subject())
        cert.set_pubkey(req.get_pubkey())
        if commonname[0] == '.':
            sans = ['*' + commonname] + \
                [s for s in sans if s != '*' + commonname]
        else:
            sans = [commonname] + [s for s in sans if s != commonname]
        #cert.add_extensions([OpenSSL.crypto.X509Extension(b'subjectAltName', True, ', '.join('DNS: %s' % x for x in sans))])
        cert.sign(key, ca_digest)

        with open(certfile, 'wb') as fp:
            fp.write(OpenSSL.crypto.dump_certificate(
                OpenSSL.crypto.FILETYPE_PEM, cert))
            fp.write(OpenSSL.crypto.dump_privatekey(
                OpenSSL.crypto.FILETYPE_PEM, pkey))
        return certfile





