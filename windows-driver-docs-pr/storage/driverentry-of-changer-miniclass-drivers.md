---
title: DriverEntry of Changer Miniclass Drivers Routine
description: In Microsoft Windows 2000, changer miniclass drivers do not have a DriverEntry routine, but in Windows XP and later operating systems a miniclass driver must have a DriverEntry routine with the following characteristics.
keywords: ["DriverEntry routine Storage Devices"]
topic_type:
- apiref
ms.topic: reference
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 10/17/2018
---

# DriverEntry of Changer Miniclass Drivers routine


In Microsoft Windows 2000, changer miniclass drivers do not have a **DriverEntry** routine, but in Windows XP and later operating systems a miniclass driver must have a **DriverEntry** routine with the following characteristics.

## Syntax

```ManagedCPlusPlus
NTSTATUS DriverEntry(
  _In_ PVOID Argument1,
  _In_ PVOID Argument2
);
```

## Parameters

*Argument1* \[in\]  
Pointer to operating system-specific information.

*Argument2* \[in\]  
Pointer to operating system-specific information.

## Return value

The miniclass driver's **DriverEntry** routine must return the value returned by the [**ChangerClassInitialize**](/windows-hardware/drivers/ddi/mcd/nf-mcd-changerclassinitialize) routine.

## Remarks

Parameters **Argument1** and **Argument2** point to operating system-specific information. A Miniclass driver should *not* attempt to interpret these parameters. Instead, it should pass these parameters to the **ChangerClassInitialize** routine.

**ChangerClassInitialize** performs most of the initialization required by the miniclass driver. The principal task of the minidriver in its **DriverEntry** routine is to load the entry points to its command processing routines into an [**MCD\_INIT\_DATA**](/windows-hardware/drivers/ddi/mcd/ns-mcd-_mcd_init_data) structure and pass the address of this structure to the **ChangerClassInitialize** routine.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Mcd.h (include Mcd.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">NtosKrnl.lib</td>
</tr>
<tr class="even">
<td align="left"><p>DLL</p></td>
<td align="left">NtosKrnl.exe</td>
</tr>
</tbody>
</table>

## <span id="see_also"></span>See also


[**ChangerClassInitialize**](/windows-hardware/drivers/ddi/mcd/nf-mcd-changerclassinitialize)

[**MCD\_INIT\_DATA**](/windows-hardware/drivers/ddi/mcd/ns-mcd-_mcd_init_data)

 

