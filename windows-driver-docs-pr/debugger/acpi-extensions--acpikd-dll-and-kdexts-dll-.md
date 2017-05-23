---
title: ACPI Extensions (Acpikd.dll and Kdexts.dll)
description: ACPI Extensions (Acpikd.dll and Kdexts.dll)
ms.assetid: 1b1df290-b65b-4066-baf5-0f283990467f
keywords: ["ACPI debugging, extensions (acpikd.dll and kdexts.dll)", "acpikd.dll (ACPI extensions)", "extensions, ACPI"]
ms.author: windowsdriverdev
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ACPI Extensions (Acpikd.dll and Kdexts.dll)


## <span id="ddk_acpi_extensions_acpikd_dll_and_kdexts_dll__dbg"></span><span id="DDK_ACPI_EXTENSIONS_ACPIKD_DLL_AND_KDEXTS_DLL__DBG"></span>


Extension commands that are useful for debugging ACPI (Advanced Configuration and Power Interface) BIOS code can be found in Acpikd.dll and Kdexts.dll.

The Windows 2000 versions of these extension commands appear in the Acpikd.dll module located in the W2kfre and W2kchk directories. Note that this extension module has an internal build number of 2179, while Windows 2000 has a build number of 2195. You should ignore the resulting version mismatch errors.

For Windows XP and later versions of Windows, some of the ACPI debugging extensions can be found in Winxp\\Acpikd.dll, while others can be found in Winxp\\Kdexts.dll.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20ACPI%20Extensions%20%28Acpikd.dll%20and%20Kdexts.dll%29%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




