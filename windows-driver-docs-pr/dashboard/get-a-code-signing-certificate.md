---
title: Get an extended validation (EV) code signing certificate
description: Get an extended validation (EV) code signing certificate
ms.topic: article
ms.date: 02/28/2022
---

# Get an extended validation (EV) code signing certificate

This article describes how to get an extended validation (EV) code signing certificate. If you've already set up a Partner Center account and need to renew a certificate, see [Add or Update a code signing certificate](update-a-code-signing-certificate.md).

Microsoft requires, as part of the Microsoft Trusted Root Certificate Program, an EV code signing certificate to register for and create a Partner Center account.

Your account must adhere to the following rules:

* Your registered EV certificate must be valid at the time of submission.
* While Microsoft strongly recommends that you sign individual submissions with an EV certificate, you can alternatively sign submissions with an Authenticode signing certificate that is also registered to your Partner Center account.
* All certificates must be SHA2 and signed with the `/fd sha256` SignTool command line switch.

If you already have an approved EV certificate from one of these authorities, you can use it to establish a Partner Center account.

## Buy a new EV certificate

To buy a new EV certificate:

1. Go to the page of one the following certificate authorities and follow the directions for purchase:

    * [DigiCert EV code signing certificate](https://www.digicert.com/order/order-1.php)
    * [Entrust EV code signing certificate](https://www.entrustdatacard.com/products/digital-signing-certificates/code-signing-certificates)
    * [GlobalSign EV code signing certificate](https://go.microsoft.com/fwlink/p/?LinkId=620888)
    * [SSL.com EV code signing certificate](https://www.ssl.com/certificates/ev-code-signing/)

1. Once the certificate authority has verified your contact information and your certificate purchase is approved, follow their directions to retrieve the certificate.

## Next steps

> [!div class="nextstepaction"]
> [Add or Update a code signing certificate](update-a-code-signing-certificate.md)

