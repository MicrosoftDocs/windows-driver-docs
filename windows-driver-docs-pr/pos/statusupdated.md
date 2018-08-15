---
title: StatusUpdated
description: StatusUpdated
ms.assetid: 'e5d04e61-859a-49ee-bc54-58be4133b38a'
ms.localizationpriority: medium
---

# StatusUpdated


This device-specific event represents events such as a power change notification.

The data buffer for this event is as follows.

Syntax
------

``` syntax
typedef struct _PosStatusUpdatedEventData
{
    PosEventDataHeader Header;
    UINT32 Status;
    UINT32 ExtendedStatus;
} PosStatusUpdatedEventData;
```

The following table shows the memory layout of the data buffer for this event.

| Memory value    | Description |
|-----------------| -------------------------------------------|
| 0x00000002 | **Header.EventType = PosEventType::StatusUpdated**  |
| 0x00000010 | **Header.DataLength** = sizeof(**PosEventDataHeader**) + sizeof(**PosStatusUpdatedEventData.Status** + sizeof(**PosStatusUpdatedEventData.ExtendedStatus**) |
| UINT32     | **Status**. See [BarcodeStatus](https://msdn.microsoft.com/library/windows/hardware/dn757472).   |
| UINT32     | **ExtendedStatus** |



Requirements
------------

**Header:** pointofservicedriverinterface.h










