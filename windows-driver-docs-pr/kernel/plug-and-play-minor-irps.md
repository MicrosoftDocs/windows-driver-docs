---
title: Plug and Play Minor IRPs
author: windows-driver-content
description: Plug and Play Minor IRPs
ms.author: windowsdriverdev
ms.date: 08/12/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.assetid: eeb7dafd-fb44-4fb7-b5f0-314059ee0093
---

# Plug and Play Minor IRPs


## <a href="" id="ddk-plug-and-play-minor-irps-dr"></a>


This section describes the PnP IRPs that are sent to drivers. All PnP IRPs have the major function code [**IRP\_MJ\_PNP**](irp-mj-pnp.md) and a minor function code indicating the particular PnP request.

This section provides reference information for the individual IRPs. See [Plug and Play](https://msdn.microsoft.com/library/windows/hardware/ff547125) for a description of the order in which the IRPs are sent, a discussion of how to handle IRPs in [DispatchPnP routines](https://msdn.microsoft.com/library/windows/hardware/ff543348), and a general discussion of PnP concepts and terminology.

For each IRP and each kind of driver, a driver is either required to handle the IRP, can optionally handle the IRP, or must not handle the IRP. Consult the table below to identify which IRPs your driver will handle and then consult the reference pages for information about the individual IRPs. The IRPs are listed in functional order in the table and in alphabetical order in the IRP reference pages.

If an IRP is marked "No" in the table for a particular driver, that driver must not handle the IRP. The driver must pass the IRP to the next driver in the device stack as described in the reference page for the IRP.

The PnP manager sends these IRPs. PnP drivers can send some of these IRPs, but only those so noted in this section.

The following are the minor function codes for PnP IRPs, and the driver types that handle them:

PnP IRP minor function code
Function or filter driver for nonbus device
Function driver for bus device (for bus FDO)
Bus driver or bus filter driver (for child PDOs)
[**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md)

Required

Required

Required

[**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md)

Required

Required

Required

[**IRP\_MN\_STOP\_DEVICE**](irp-mn-stop-device.md)

Required

Required

Required

[**IRP\_MN\_CANCEL\_STOP\_DEVICE**](irp-mn-cancel-stop-device.md)

Required

Required

Required

[**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md)

Required

Required

Required

[**IRP\_MN\_REMOVE\_DEVICE**](irp-mn-remove-device.md)

Required

Required

Required

[**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](irp-mn-cancel-remove-device.md)

Required

Required

Required

[**IRP\_MN\_SURPRISE\_REMOVAL**](irp-mn-surprise-removal.md)

Required

Required

Required

[**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md)

Optional

Optional

Required

[**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](irp-mn-query-pnp-device-state.md)

Optional

Optional

Optional

[**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](irp-mn-filter-resource-requirements.md)

Optional (1)

Optional (1)

No

[**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](irp-mn-device-usage-notification.md)

Required (1)

Required (1)

Required (1)

[**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](irp-mn-query-device-relations.md)

-   **BusRelations**

Optional (1)

Required

No (2)

-   **EjectionRelations**

No

No

Optional

-   **RemovalRelations**

Optional

Optional

No

-   **TargetDeviceRelation**

No

No

Required

[**IRP\_MN\_QUERY\_RESOURCES**](irp-mn-query-resources.md)

No

No

Required (1)

[**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](irp-mn-query-resource-requirements.md)

No

No

Required (1)

[**IRP\_MN\_QUERY\_ID**](irp-mn-query-id.md)

-   **BusQueryDeviceID**

No

No

Required

-   **BusQueryHardwareIDs**

No

No

Optional

-   **BusQueryCompatibleIDs**

No

No

Optional

-   **BusQueryInstanceID**

No

No

Optional

-   **BusQueryContainerID**

No

No

Required (3)

[**IRP\_MN\_QUERY\_DEVICE\_TEXT**](irp-mn-query-device-text.md)

No

No

Required (1)

[**IRP\_MN\_QUERY\_BUS\_INFORMATION**](irp-mn-query-bus-information.md)

No

No

Required (1)

[**IRP\_MN\_QUERY\_INTERFACE**](irp-mn-query-interface.md)

Optional

Optional

Required (1)

[**IRP\_MN\_READ\_CONFIG**](irp-mn-read-config.md)

No

No

Required (1)

[**IRP\_MN\_WRITE\_CONFIG**](irp-mn-write-config.md)

No

No

Required (1)

[**IRP\_MN\_DEVICE\_ENUMERATED**](irp-mn-device-enumerated.md)

No

No

Required (1)

[**IRP\_MN\_SET\_LOCK**](irp-mn-set-lock.md)

No

No

Required (1)

(1) Required or optional in certain situations. See the reference page for the IRP for more details.

(2) Bus filter drivers might handle a query for **BusRelations**.

(3) Supported in Windows 7 and later versions of Windows.

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Plug%20and%20Play%20Minor%20IRPs%20%20RELEASE:%20%288/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


