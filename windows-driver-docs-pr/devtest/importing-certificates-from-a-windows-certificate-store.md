---
title: Importing Certificates from a Windows Certificate Store
description: Importing Certificates from a Windows Certificate Store
ms.assetid: abdf19c7-2cea-4af3-8a86-37fc4a9e7c3d
---

# Importing Certificates from a Windows Certificate Store


You can use the Enhanced Storage Certificate Management tool to import certificates from your private certificate store in the computer to an IEEE 1667-compliant USB storage device.

To import a certificate from a private certificate store, you must specify the certificate name by using the **-Store** parameter of the [**/Add**](enhstor-add-switch.md) and [**/Replace**](-replace-switch.md) switches of the Enhanced Storage Certificate Management tool. The tool searches all of your private certificate stores for the specified certificate and (if found) imports it to a specified USB storage device.

**Note**  The tool does not import a certificate from the Windows root certificate store.

 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Importing%20Certificates%20from%20a%20Windows%20Certificate%20Store%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




