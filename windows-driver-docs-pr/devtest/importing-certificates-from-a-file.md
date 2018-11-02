---
title: Importing Certificates from a File
description: Importing Certificates from a File
ms.assetid: 17596119-6b31-4a69-b83c-cec1dfd55572
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Importing Certificates from a File


You can use the Enhanced Storage Certificate Management tool to import certificates from a file. The file must contain an X.509 certificate that is encoded in a Distinguished Encoding Rules (DER) binary format.

You can create this file by using one of the following methods:

-   The certificate can be exported by the Enhanced Storage Certificate Management tool from an IEEE 1667-compliant USB storage device. The tool saves the certificate in a file that is specified when the tool is executed.

    For more information, see to the [**/Export switch**](-export-switch.md) of the Enhanced Storage Certificate Management tool.

-   The certificate can be created by using the [**MakeCert**](makecert.md) utility and saved in the file.

-   The certificate can be created by using any application that can generate an X.509 certificate that is encoded in DER binary format. The certificate is then saved in the file.

For more information about how to import a certificate from a file to an IEEE 1667-compliant USB storage device, see the **-File** parameter of the [**/Add**](enhstor-add-switch.md) and [**/Replace**](-replace-switch.md) switches of the Enhanced Storage Certificate Management tool.

 

 





