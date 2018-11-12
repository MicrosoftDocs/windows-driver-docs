---
title: Debugging BIOS Code
description: Debugging BIOS Code
ms.assetid: 98f0381b-4f9d-4cf2-9860-8da20f6fbd38
keywords: ["BIOS debugging", "BIOS debugging, overview"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Debugging BIOS Code


## <span id="ddk_debugging_bios_code_dbg"></span><span id="DDK_DEBUGGING_BIOS_CODE_DBG"></span>


BIOS code is not built from standard assembly code, so it requires different debugging techniques.

On an x86-based processor, the BIOS uses 16-bit code. To disassemble this code, use the [**ux (Unassemble x86 BIOS)**](ux--unassemble-x86-bios-.md) command. To display information about the Intel Multiprocessor Specification (MPS), use the [**!mps**](-mps.md) extension.

If you are debugging ACPI BIOS code, the preceding commands do not work, because ACPI BIOS is written in ACPI Machine Language (AML). To disassemble this code, you should use [**!amli u**](-amli-u.md). For more information about this kind of debugging, see [ACPI Debugging](acpi-debugging.md).

 

 





