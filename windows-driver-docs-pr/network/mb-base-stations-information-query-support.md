---
title: MB base stations information query support
description: MB base stations information query support
ms.assetid: 200954a6-0f6c-4c00-86cb-510399f7b713
keywords:
- MB base stations information query, Mobile Broadband base stations information query
ms.author: windowsdriverdev
ms.date: 08/14/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# MB base stations information query support

## Overview

The base stations information query interface is used to provide location based services with cellular base station information, such as *Base Station ID*, *Time Advance*, and other parameters that can be used to compute the geographical position of the mobile subscriber. The information gathered pertains to the cellular base station currently serving the subscriber, as well as neighboring cellular base stations. 

This topic defines the base stations information query interface for Windows, as the MBIM 1.0 specification does not provide this information through any existing CIDs. This interface is available in Windows 10, version 1709 and later. 

Serving and neighbor cell parameters are retrieved via Query/Response operations. A notification is also defined in this topic to indicate that the location of the device within the cellular network has changed.

## MBIM_CID_BASE_STATIONS_INFO

This command retrieves information about the serving and neighbor cells known to the modem.

Service: **MBB_UUID_BASIC_CONNECT_EXTENSIONS**

Service UUID: **3d01dcc5-fef5-4d05-0d3a-bef7058e9aaf**

### Parameters

| | Set | Query | Notification |
| --- | --- | --- | --- |
| Command | Not applicable | MBIM_BASE_STATIONS_INFO_REQ | Not applicable |
| Response | Not appliable | MBIM_BASE_STATIONS_INFO | Not applicable |

### Query

The following MBIM_BASE_STATIONS_INFO_REQ structure shall be used in the InformationBuffer. It is used to configure aspects of the cell information, such as the maximum number of neighbor cell measurements, to send in response. 

| Offset | Size | Field | Type | Description |
| --- | --- | --- | --- | --- |


[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Slicer%20settings%20%20RELEASE:%20%289/2/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")