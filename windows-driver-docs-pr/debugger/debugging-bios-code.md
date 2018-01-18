---
title: Debugging BIOS Code
description: Debugging BIOS Code
ms.assetid: 98f0381b-4f9d-4cf2-9860-8da20f6fbd38
keywords: ["BIOS debugging", "BIOS debugging, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Debugging BIOS Code


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


BIOS code is not built from standard assembly code, so it requires different debugging techniques.

On an x86-based processor, the BIOS uses 16-bit code. To disassemble this code, use the [**ux (Unassemble x86 BIOS)**](ux--unassemble-x86-bios-.md) command. To display information about the Intel Multiprocessor Specification (MPS), use the [**!mps**](-mps.md) extension.

If you are debugging ACPI BIOS code, the preceding commands do not work, because ACPI BIOS is written in ACPI Machine Language (AML). To disassemble this code, you should use [**!amli u**](-amli-u.md). For more information about this kind of debugging, see [ACPI Debugging](acpi-debugging.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Debugging%20BIOS%20Code%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




