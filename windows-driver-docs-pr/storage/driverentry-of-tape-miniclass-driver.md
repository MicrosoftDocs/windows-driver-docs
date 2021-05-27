---
title: DriverEntry of Tape Miniclass Driver routine
description: DriverEntry initializes a tape miniclass driver. This routine is required.
keywords: ["DriverEntry routine Storage Devices"]
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DriverEntry of Tape Miniclass Driver routine


**DriverEntry** initializes a tape miniclass driver. This routine is required.

## Syntax

```ManagedCPlusPlus
ULONG DriverEntry(
  _In_ PVOID Argument1,
  _In_ PVOID Argument2
);
```

## Parameters

*Argument1* \[in\]  
Pointer to a driver context that a tape miniclass driver passes to [**TapeClassInitialize**](/windows-hardware/drivers/ddi/minitape/nf-minitape-tapeclassinitialize). The format of the context information is OS-specific and must not be interpreted by portable tape miniclass drivers.

*Argument2* \[in\]  
Pointer to a second context structure that a tape miniclass driver passes to **TapeClassInitialize**. The format of the context information is OS-specific and must not be interpreted by portable tape miniclass drivers.

## Return value

**DriverEntry** returns the value returned by its call to **TapeClassInitialize**.

## Remarks

**DriverEntry** is the initial entry point for a tape miniclass driver.

Since **TapeClassInitialize** performs most of the required driver initialization, the primary task of a tape miniclass driver's **DriverEntry** routine is to allocate and fill in a TAPE\_INIT\_DATA\_EX structure with driver-specific constants and entry points.

**DriverEntry** first must call [**TapeClassZeroMemory**](/windows-hardware/drivers/ddi/minitape/nf-minitape-tapeclasszeromemory) to clear the TAPE\_INIT\_DATA\_EX structure. **DriverEntry** then sets the values and pointers in the structure.

**DriverEntry** calls **TapeClassInitialize** and passes the address of TAPE\_INIT\_DATA\_EX and the two pointers that were passed to **DriverEntry** (*Argument1* and *Argument2*). **TapeClassInitialize** completes driver initialization and returns status to the tape miniclass driver's **DriverEntry** routine. **DriverEntry** returns the status that it received from **TapeClassInitialize**.

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
<td align="left">Minitape.h</td>
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


[**TAPE\_INIT\_DATA\_EX**](/windows-hardware/drivers/ddi/minitape/ns-minitape-_tape_init_data_ex)

[**TapeClassInitialize**](/windows-hardware/drivers/ddi/minitape/nf-minitape-tapeclassinitialize)

[**TapeClassZeroMemory**](/windows-hardware/drivers/ddi/minitape/nf-minitape-tapeclasszeromemory)

[**TAPE\_STATUS**](/windows-hardware/drivers/ddi/minitape/ne-minitape-_tape_status)

 

