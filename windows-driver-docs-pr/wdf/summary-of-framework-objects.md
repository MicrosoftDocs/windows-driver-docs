---
title: Summary of Framework Objects
description: Summary of Framework Objects
keywords:
- framework objects WDK KMDF , listed
- framework objects WDK KMDF , summary
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Summary of Framework Objects


The following table lists all of the framework objects and provides some basic information about each object. The mode column indicates whether the object can be used in KMDF and UMDF drivers, or KMDF only.

For a list of callbacks and methods and which frameworks are applicable, see [Summary of WDF Callbacks and Methods](/windows-hardware/drivers/ddi/_wdf/).

|Name|Handle|Purpose|Default parent|Can driver override default parent?|Mode|Reference|
|--- |--- |--- |--- |--- |--- |--- |
|Child-list object|WDFCHILDLIST|Represents a list of child devices that are connected to a parent device.|Device object|No|KM|[WDF Child-List Object Reference](/windows-hardware/drivers/ddi/wdfchildlist/)|
|Collection object|WDFCOLLECTION|Represents an object collection.|Driver object|Yes|KM/UM|[WDF Collection Object Reference](/windows-hardware/drivers/ddi/wdfcollection/)|
|Common buffer object|WDFCOMMONBUFFER|Represents a common buffer.|DMA enabler object|No|KM|[WDF Common Buffer Object Reference](/windows-hardware/drivers/ddi/wdfcommonbuffer/)|
|Device object|WDFDEVICE|Represents a device.|Driver object|No|KM/UM|[WDF Device Object Reference](/windows-hardware/drivers/ddi/wdfdevice/)|
|DMA enabler object|WDFDMAENABLER|Enables a driver to use the framework's DMA capabilities.|Device object|Yes|KM|[WDF DMA Object Reference](/windows-hardware/drivers/ddi/wdfdmaenabler/)|
|DMA transaction object|WDFDMATRANSACTION|Represents a DMA transaction.|DMA enabler object|No|KM|[WDF DMA Object Reference](/windows-hardware/drivers/ddi/wdfdmaenabler/)|
|DPC object|WDFDPC|Represents a deferred procedure call.|None|Yes|KM|[WDF DPC Object Reference](/windows-hardware/drivers/ddi/wdfdpc/)|
|Driver object|WDFDRIVER|Represents a driver.|None|No|KM/UM|[WDF Driver Object Reference](/windows-hardware/drivers/ddi/wdfdriver/)|
|File object|WDFFILEOBJECT|Represents a file.|Device object|No|KM/UM|[WDF File Object Reference](/windows-hardware/drivers/ddi/wdffileobject/)|
|General object|WDFOBJECT|Represents a general object.|Driver object|Yes|KM/UM|[WDF General Object Reference](/windows-hardware/drivers/ddi/wdfobject/)|
|Interrupt object|WDFINTERRUPT|Represents a hardware interrupt resource.|Device object|Yes|KM/UM|[WDF Interrupt Object Reference](/windows-hardware/drivers/ddi/wdfinterrupt/)|
|I/O target object|WDFIOTARGET|Represents a driver to which another driver sends I/O requests.|Device object|Yes|KM/UM|[WDF I/O Target Object Reference](/windows-hardware/drivers/ddi/wdfiotarget/)|
|Lookaside-list object|WDFLOOKASIDE|Represents a lookaside list.|Driver object|Yes|KM|[WDF Memory Object Reference](/windows-hardware/drivers/ddi/wdfmemory/)|
|Memory object|WDFMEMORY|Represents a memory buffer.|Driver object|Yes|KM/UM|[WDF Memory Object Reference](/windows-hardware/drivers/ddi/wdfmemory/)|
|Queue object|WDFQUEUE|Represents an I/O queue that receives I/O requests.|Device object|Yes|KM/UM|[WDF Queue Object Reference](/windows-hardware/drivers/ddi/wdfio/)|
|Registry key object|WDFKEY|Represents a registry key.|Driver object|Yes|KM/UM|[WDF Registry Key Object Reference](/windows-hardware/drivers/ddi/wdfregistry/)|
|Request object|WDFREQUEST|Represents an I/O request.|None, if created by framework. Driver object, if created by driver.|Yes, if created by driver.|KM/UM|[WDF Request Object Reference](/windows-hardware/drivers/ddi/wdfrequest/)|
|Resource list object|WDFCMRESLIST|Represents a resource list.|Driver object|No|KM/UM|[WDF Resource Object Reference](/windows-hardware/drivers/ddi/wdfresource/)|
|Resource range list object|WDFIORESLIST|Represents a logical configuration.|Resource requirements list object|No|KM|[WDF Resource Object Reference](/windows-hardware/drivers/ddi/wdfresource/)|
|Resource requirements list object|WDFIORESREQLIST|Represents a resource requirements list.|Driver object|No|KM|[WDF Resource Object Reference](/windows-hardware/drivers/ddi/wdfresource/)|
|Spin-lock object|WDFSPINLOCK|Represents a spin lock.|Driver object|Yes|KM/UM|[WDF Synchronization Methods](/windows-hardware/drivers/ddi/wdfsync/)|
|String object|WDFSTRING|Represents a Unicode string.|Driver object|Yes|KM/UM|[WDF String Object Reference](/windows-hardware/drivers/ddi/wdfstring/)|
|Timer object|WDFTIMER|Represents a timer.|None|Yes|KM/UM|[WDF Timer Object Reference](/windows-hardware/drivers/ddi/wdftimer/)|
|USB device object|WDFUSBDEVICE|Represents a device connected to a USB.|Device object|No|KM/UM|[WDF USB Reference](/windows-hardware/drivers/ddi/wdfusb/)|
|USB interface object|WDFUSBINTERFACE|Represents a USB device interface.|USB device object|No|KM/UM|[WDF USB Reference](/windows-hardware/drivers/ddi/wdfusb/)|
|USB pipe object|WDFUSBPIPE|Represents a USB device pipe.|USB interface object|No|KM/UM|[WDF USB Reference](/windows-hardware/drivers/ddi/wdfusb/)|
|Wait-lock object|WDFWAITLOCK|Represents a wait lock.|Driver object|Yes|KM/UM|[WDF Synchronization Methods](/windows-hardware/drivers/ddi/wdfsync/)|
|WMI instance object|WDFWMIINSTANCE|Represents an instance of a WMI data block.|WMI provider object|No|KM|[WDF WMI Reference](/windows-hardware/drivers/ddi/wdfwmi/)|
|WMI provider object|WDFWMIPROVIDER|Represents a WMI data block.|Device object|No|KM|[WDF WMI Reference](/windows-hardware/drivers/ddi/wdfwmi/)|
|Work-item object|WDFWORKITEM|Represents a work item.|None|Yes|KM/UM|[WDF Work-Item Object Reference](/windows-hardware/drivers/ddi/wdfworkitem/)|


 

 

