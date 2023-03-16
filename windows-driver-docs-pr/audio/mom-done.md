---
title: MOM_DONE function (Windows Drivers)
description: Learn more about the MOM_DONE function.
keywords:
- mmddk/modMessage
- modMessage
ms.date: 03/06/2023
ms.topic: reference
---

# MOM\_DONE function

WINMM sends the **MOM\_DONE** message to the [**modMessage**](mod-message.md) function of MIDI output driver, to return a system-exclusive data block to the client application.

## Syntax

``` c++
DWORD modMessage(
   UINT      uDeviceID,
   UINT      uMsg,
   DWORD_PTR dwUser,
   DWORD_PTR dwParam1,
   DWORD_PTR dwParam2
);
```

## Parameters

- *uDeviceID*  
  Specifies the ID of the target device. Device IDs are sequential that has an initial value of zero and a final value that is equal to one less than the number of devices that the driver supports.

- *uMsg*  
  WINMM sets this parameter to **MOM\_DONE** when it calls [**modMessage**](mod-message.md) to process this message.

- *dwUser*  
  The driver sets this parameter to match the instance data from the client that called it.

- *dwParam1*  
  Specifies a far pointer to a [MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr) structure that identifies the data block.

- *dwParam2*  
  Not used.

## Return value

None

## Remarks

## Requirements

<table>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>Desktop</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Available in Windows XP and later Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Mmddk.h (include Mmddk.h, Mmsystem.h, or Windows.h)</td>
</tr>
</tbody>
</table>

## See also

[MIDIHDR](/windows/win32/api/mmeapi/ns-mmeapi-midihdr)
