---
title: Importing Certificates from a File
description: Importing Certificates from a File
ms.assetid: 17596119-6b31-4a69-b83c-cec1dfd55572
---

# Importing Certificates from a File


You can use the Enhanced Storage Certificate Management tool to import certificates from a file. The file must contain an X.509 certificate that is encoded in a Distinguished Encoding Rules (DER) binary format.

You can create this file by using one of the following methods:

-   The certificate can be exported by the Enhanced Storage Certificate Management tool from an IEEE 1667-compliant USB storage device. The tool saves the certificate in a file that is specified when the tool is executed.

    For more information, see to the [**/Export switch**](-export-switch.md) of the Enhanced Storage Certificate Management tool.

-   The certificate can be created by using the [**MakeCert**](makecert.md) utility and saved in the file.

-   The certificate can be created by using any application that can generate an X.509 certificate that is encoded in DER binary format. The certificate is then saved in the file.

For more information about how to import a certificate from a file to an IEEE 1667-compliant USB storage device, see the **-File** parameter of the [**/Add**](enhstor-add-switch.md) and [**/Replace**](-replace-switch.md) switches of the Enhanced Storage Certificate Management tool.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Importing%20Certificates%20from%20a%20File%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




