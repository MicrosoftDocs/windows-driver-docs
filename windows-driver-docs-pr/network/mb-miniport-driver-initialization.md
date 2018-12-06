---
title: MB Miniport Driver Initialization
description: MB Miniport Driver Initialization
ms.assetid: cf332eb4-faea-40e3-b313-512f81718267
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# MB Miniport Driver Initialization


The following diagram represents the process taken to determine whether the interface is qualified as an MB interface and to gather information about the device capabilities. These steps are performed for each enumerated MB interface when the MB Service starts up, as well as for each new interface arrival while the service is running. The labels in bold represent OID identifiers or transactional flow control, and the labels in regular text represent the important flags within the OID structure.

![diagram illustrating establishing if the interface is qualified as an mb interface, and illustrating gathering information about device capabilities](images/wwandriverinitproc.png)

To initialize an MB miniport driver, use the following procedure:

1.  The MB Service sends a synchronous (blocking) [OID\_GEN\_PHYSICAL\_MEDIUM](https://msdn.microsoft.com/library/windows/hardware/ff569621) query request to identify the type of the MB device. The miniport driver responds with **NdisPhysicalMediumWirelessWan** to indicate that the MB device is a WWAN device.

2.  The MB Service sends a synchronous (blocking) [OID\_GEN\_MEDIA\_SUPPORTED](https://msdn.microsoft.com/library/windows/hardware/ff569609) query request to the miniport driver to identify what kind of medium the MB device uses. The miniport driver responds with **NdisMedium802\_3** to indicate that it uses Ethernet emulation.

3.  The MB Service sends a synchronous (blocking) [OID\_WWAN\_DRIVER\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569825) query request to the miniport driver to identify what driver model version the miniport driver supports. The miniport driver responds with WWAN\_VERSION.

4.  The MB Service sends an asynchronous (non-blocking) [OID\_WWAN\_DEVICE\_CAPS](https://msdn.microsoft.com/library/windows/hardware/ff569824) query request to the miniport driver to identify the capabilities of the MB device. The miniport driver responds with a provisional acknowledgement that it has received the request, and it will send a notification with the requested information in the future.

5.  The miniport driver sends an [**NDIS\_STATUS\_WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567845) notification to the MB Service that indicates the capabilities of the MB device the miniport driver supports. For example, if the miniport driver supports a GSM-based device, it should specify the **WwanCellularClassGsm** value in the **DeviceCaps.WwanCellularClass** member of the [**NDIS\_WWAN\_DEVICE\_CAPS**](https://msdn.microsoft.com/library/windows/hardware/ff567907) structure. If the miniport driver supports a CDMA-based device, it should specify **WwanCellularClassCdma**.

 

 





