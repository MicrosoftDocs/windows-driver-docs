---
title: KSRTAUDIO\_BUFFER\_PROPERTY structure
description: The KSRTAUDIO\_BUFFER\_PROPERTY structure appends a buffer base address and requested buffer size to a KSPROPERTY structure. This structure is used by the client to request allocation of the audio buffer via KSPROPERTY\_RTAUDIO\_BUFFER.
ms.assetid: 6fc33d5d-5d7e-4d04-a9b0-864cba961077
keywords: ["KSRTAUDIO_BUFFER_PROPERTY structure Audio Devices", "PKSRTAUDIO_BUFFER_PROPERTY structure pointer Audio Devices"]
topic_type:
- apiref
api_name:
- KSRTAUDIO_BUFFER_PROPERTY
api_location:
- ksmedia.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSRTAUDIO\_BUFFER\_PROPERTY structure


The KSRTAUDIO\_BUFFER\_PROPERTY structure appends a buffer base address and requested buffer size to a [**KSPROPERTY**](https://msdn.microsoft.com/library/windows/hardware/ff564262) structure. This structure is used by the client to request allocation of the audio buffer via [**KSPROPERTY\_RTAUDIO\_BUFFER**](ksproperty-rtaudio-buffer.md).

Syntax
------

```ManagedCPlusPlus
typedef struct {
  KSPROPERTY Property;
  PVOID      BaseAddress;
  ULONG      RequestedBufferSize;
} KSRTAUDIO_BUFFER_PROPERTY, *PKSRTAUDIO_BUFFER_PROPERTY;
```

Members
-------

**Property**  
A KSPROPERTY structure that the client initializes appropriately prior to calling KSPROPERTY\_RTAUDIO\_BUFFER.

**BaseAddress**  
Specifies the desired buffer base address. Unless the client specifies a base address, this parameter is set to **NULL**.

**RequestedBufferSize**  
Specifies the desired buffer size in bytes. The driver returns the actual size of the allocated buffer in the [**KSRTAUDIO\_BUFFER**](https://msdn.microsoft.com/library/windows/hardware/ff537493) structure that it returns.

Remarks
-------

The KSPROPERTY\_RTAUDIO\_BUFFER request uses the KSRTAUDIO\_BUFFER\_PROPERTY structure to describe the cyclic buffer that the client requests. The driver returns a KSRTAUDIO\_BUFFER structure to describe the buffer that was actually allocated.

The value that the client writes into the **RequestedBufferSize** member is not binding on the driver. However, the driver must specify a buffer size that is as close as possible to the requested size, taking into account the buffer size constraints on the driver itself. The driver allocates a buffer of a different size if the hardware cannot handle the requested size or the system is low on memory. For example, a driver allocates a buffer no smaller than a memory page, or it rounds the buffer size down to the next whole sample block. Also, if the system is running low on memory, the driver allocates a buffer that is smaller than the requested size.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later Windows operating systems.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ksmedia.h</td>
</tr>
</tbody>
</table>

 

 





