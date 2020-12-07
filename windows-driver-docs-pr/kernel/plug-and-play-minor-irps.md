---
title: Plug and Play Minor IRPs
description: Plug and Play Minor IRPs
ms.date: 08/12/2017
ms.localizationpriority: medium
---

# Plug and Play Minor IRPs





This section describes the PnP IRPs that are sent to drivers. All PnP IRPs have the major function code [**IRP\_MJ\_PNP**](irp-mj-pnp.md) and a minor function code indicating the particular PnP request.

This section provides reference information for the individual IRPs. See [Plug and Play](./introduction-to-plug-and-play.md) for a description of the order in which the IRPs are sent, a discussion of how to handle IRPs in [DispatchPnP routines](./dispatchpnp-routines.md), and a general discussion of PnP concepts and terminology.

For each IRP and each kind of driver, a driver is either required to handle the IRP, can optionally handle the IRP, or must not handle the IRP. Consult the table below to identify which IRPs your driver will handle and then consult the reference pages for information about the individual IRPs. The IRPs are listed in functional order in the table and in alphabetical order in the IRP reference pages.

If an IRP is marked "No" in the table for a particular driver, that driver must not handle the IRP. The driver must pass the IRP to the next driver in the device stack as described in the reference page for the IRP.

The PnP manager sends these IRPs. PnP drivers can send some of these IRPs, but only those so noted in this section.

The following are the minor function codes for PnP IRPs, and the driver types that handle them:


|                              PnP IRP minor function code                              | Value | Function or filter driver for nonbus device | Function driver for bus device (for bus FDO) | Bus driver or bus filter driver (for child PDOs) |
|---------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------|--------------------------------------------------|
|                 [**IRP\_MN\_START\_DEVICE**](irp-mn-start-device.md)                  |0x00|                  Required                   |                   Required                   |                     Required                     |
|          [**IRP\_MN\_QUERY\_REMOVE\_DEVICE**](irp-mn-query-remove-device.md)          |0x01|                  Required                   |                   Required                   |                     Required                     |
|                [**IRP\_MN\_REMOVE\_DEVICE**](irp-mn-remove-device.md)                 |0x02|                  Required                   |                   Required                   |                     Required                     |
|         [**IRP\_MN\_CANCEL\_REMOVE\_DEVICE**](irp-mn-cancel-remove-device.md)         |0x03|                  Required                   |                   Required                   |                     Required                     |
|                  [**IRP\_MN\_STOP\_DEVICE**](irp-mn-stop-device.md)                   |0x04|                  Required                   |                   Required                   |                     Required                     |
|            [**IRP\_MN\_QUERY\_STOP\_DEVICE**](irp-mn-query-stop-device.md)            |0x05|                  Required                   |                   Required                   |                     Required                     |
|           [**IRP\_MN\_CANCEL\_STOP\_DEVICE**](irp-mn-cancel-stop-device.md)           |0x06|                  Required                   |                   Required                   |                     Required                     |
|       [**IRP\_MN\_QUERY\_DEVICE\_RELATIONS**](irp-mn-query-device-relations.md)       |0x07                                             |                                              |                                                  |
|                                 -   **BusRelations**                                  |x|                Optional (1)                 |                   Required                   |                      No (2)                      |
|                               -   **EjectionRelations**                               |x|                     No                      |                      No                      |                     Optional                     |
|                               -   **RemovalRelations**                                |x|                  Optional                   |                   Optional                   |                        No                        |
|                             -   **TargetDeviceRelation**                              |x|                     No                      |                      No                      |                     Required                     |
|              [**IRP\_MN\_QUERY\_INTERFACE**](irp-mn-query-interface.md)               |0x08|                  Optional                   |                   Optional                   |                   Required (1)                   |
|           [**IRP\_MN\_QUERY\_CAPABILITIES**](irp-mn-query-capabilities.md)            |0x09|                  Optional                   |              Optional | Required               |                                                  |
|              [**IRP\_MN\_QUERY\_RESOURCES**](irp-mn-query-resources.md)               |0x0A|                     No                      |                      No                      |                   Required (1)                   |
|  [**IRP\_MN\_QUERY\_RESOURCE\_REQUIREMENTS**](irp-mn-query-resource-requirements.md)  |0x0B|                     No                      |                      No                      |                   Required (1)                   |
|            [**IRP\_MN\_QUERY\_DEVICE\_TEXT**](irp-mn-query-device-text.md)            |0x0C|                     No                      |                      No                      |                   Required (1)                   |
| [**IRP\_MN\_FILTER\_RESOURCE\_REQUIREMENTS**](irp-mn-filter-resource-requirements.md) |0x0D|                Optional (1)                 |                 Optional (1)                 |                        No                        |
|                  [**IRP\_MN\_READ\_CONFIG**](irp-mn-read-config.md)                   |0x0F|                     No                      |                      No                      |                   Required (1)                   |
|                 [**IRP\_MN\_WRITE\_CONFIG**](irp-mn-write-config.md)                  |0x10|                     No                      |                      No                      |                   Required (1)                   |
|                 [**IRP\_MN\_EJECT**](irp-mn-eject.md)                  |0x11|                     No                      |                      No                      |                   Required                   |
|                     [**IRP\_MN\_SET\_LOCK**](irp-mn-set-lock.md)                      |0x12|                     No                      |                      No                      |                   Required (1)                   |
|                     [**IRP\_MN\_QUERY\_ID**](irp-mn-query-id.md)                      |0x13|                                             |                                              |                                                  |
|                               -   **BusQueryDeviceID**                                |x|                     No                      |                      No                      |                     Required                     |
|                              -   **BusQueryHardwareIDs**                              |x|                     No                      |                      No                      |                     Optional                     |
|                             -   **BusQueryCompatibleIDs**                             |x|                     No                      |                  No  |  Optional                  |                                                  |
|                              -   **BusQueryInstanceID**                               |x|                     No                      |                      No                      |                     Optional                     |
|                              -   **BusQueryContainerID**                              |x|                     No                      |                      No                      |                   Required (3)                   |
|      [**IRP\_MN\_QUERY\_PNP\_DEVICE\_STATE**](irp-mn-query-pnp-device-state.md)       |0x14|                  Optional                   |                   Optional                   |                     Optional                     |
|        [**IRP\_MN\_QUERY\_BUS\_INFORMATION**](irp-mn-query-bus-information.md)        |0x15|                     No                      |                      No                      |                   Required (1)                   |
|    [**IRP\_MN\_DEVICE\_USAGE\_NOTIFICATION**](irp-mn-device-usage-notification.md)    |0x16|                Required (1)                 |                 Required (1)                 |                   Required (1)                   |
|             [**IRP\_MN\_SURPRISE\_REMOVAL**](irp-mn-surprise-removal.md)              |0x17|                  Required                   |                   Required                   |                     Required                     |
|            [**IRP\_MN\_DEVICE\_ENUMERATED**](irp-mn-device-enumerated.md)             |0x19|                     No                      |                      No                      |                   Required (1)                   |

(1) Required or optional in certain situations. See the reference page for the IRP for more details.

(2) Bus filter drivers might handle a query for **BusRelations**.

(3) Supported in Windows 7 and later versions of Windows.
