---
title: IWiaMiniDrv COM Interface
description: This topic provides detailed guidance on using the IWiaMiniDrv COM interface
ms.date: 05/03/2023
---

# IWiaMiniDrv COM interface

Imaging applications make requests to the WIA service, which in turn communicates with the device minidriver through the minidriver writer-implemented [IWiaMiniDrv interface](/windows-hardware/drivers/ddi/wiamindr_lh/nn-wiamindr_lh-iwiaminidrv). Applications typically make requests for:

- [Creating and initializing items](#creating-and-initializing-items)

- [Deleting items](#deleting-items)

- [Enumerating device capabilities](#enumerating-device-capabilities)

- [Enumerating image formats](#enumerating-image-formats)

- [Issuing device commands](#issuing-device-commands)

- [Locking and unlocking a device](#locking-and-unlocking-a-device)

- [Notifying a device of an event](#notifying-a-device-of-an-event)

- [Obtaining device error strings](#obtaining-device-error-strings)

- [Reading and storing item properties](#reading-and-storing-item-properties)

- [Transferring data](#transferring-data)

Applications make requests to the WIA service through the WIA application programming interface (API). For more information about this interface, see the Microsoft Windows SDK documentation.

The **IWiaMiniDrv** interface provides the entry points shown in the following tables for the WIA service to control the device. A WIA minidriver must implement every **IWiaMiniDrv** method. These entry points are defined through the following **IWiaMiniDrv** methods.

## Creating and initializing items

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvAnalyzeItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvanalyzeitem) | Inspects an item and, if necessary, creates subitems. |
| [**IWiaMiniDrv::drvInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinitializewia) | Initializes the WIA minidriver. |
| [**IWiaMiniDrv::drvInitItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvinititemproperties) | Initializes driver item properties for each item in an application item tree. |

## Deleting items

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvDeleteItem**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdeleteitem) | Deletes a driver item. |
| [**IWiaMiniDrv::drvFreeDrvItemContext**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvfreedrvitemcontext) | Frees a device-specific context. |
| [**IWiaMiniDrv::drvUnInitializeWia**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvuninitializewia) | Releases device resources associated with an application item tree. |

## Enumerating device capabilities

| Method | Description |
| -- | -- |
| [**IWiaMiniDrv::drvGetCapabilities**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetcapabilities) | Reports the events and commands supported by a WIA minidriver. |

## Enumerating image formats

| Method | Description |
| -- | -- |
| [**IWiaMiniDrv::drvGetWiaFormatInfo**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetwiaformatinfo) | Gets supported device formats and media types. |

## Issuing device commands

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvDeviceCommand**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvdevicecommand) | Issues a command to an imaging device. |

## Locking and unlocking a device

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvLockWiaDevice**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvlockwiadevice) | Locks access to an imaging device. |
| [**IWiaMiniDrv::drvUnLockWiaDevice**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvunlockwiadevice) | Unlocks access to an imaging device. |

## Notifying a device of an event

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvNotifyPnPEvent**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvnotifypnpevent) | Indicates a WIA minidriver's response to a Plug and Play event. |

## Obtaining device error strings

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvGetDeviceErrorStr**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvgetdeviceerrorstr) | Maps a device error value to a string. |

## Reading and storing item properties

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvReadItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvreaditemproperties) | Reads driver item properties. |
| [**IWiaMiniDrv::drvValidateItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvvalidateitemproperties) | Validates driver item properties. |
| [**IWiaMiniDrv::drvWriteItemProperties**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvwriteitemproperties) | Writes driver item properties to the device (if needed). |

## Transferring data

| Method | Description |
|--|--|
| [**IWiaMiniDrv::drvAcquireItemData**](/windows-hardware/drivers/ddi/wiamindr_lh/nf-wiamindr_lh-iwiaminidrv-drvacquireitemdata) | Transfers data from a driver item to the WIA service. |
