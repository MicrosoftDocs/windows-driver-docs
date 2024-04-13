---
title: Bluetooth IOCTLs
description: Bluetooth IOCTLs
keywords:
- Bluetooth WDK , IOCTLs
- IOCTLs WDK Bluetooth
- local Bluetooth WDK
- remote Bluetooth WDK
ms.date: 04/20/2017
---

# Bluetooth IOCTLs

The Bluetooth driver stack provides profile drivers with several IOCTLs to gather information about:

- The local Bluetooth radio and system.

- Remote Bluetooth devices.

- The device that caused the Plug and Play (PnP) Manager to load a profile driver.

To gather information about the local Bluetooth radio and system, a profile driver uses [**IOCTL_BTH_GET_LOCAL_INFO**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_get_local_info). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a [**BTH_LOCAL_RADIO_INFO**](/windows-hardware/drivers/ddi/bthioctl/ns-bthioctl-_bth_local_radio_info) structure that contains information about the local Bluetooth radio and system, including flags that indicate whether the local radio can be discovered and connected to. The returned BTH_LOCAL_RADIO_INFO structure contains a [BTH_DEVICE_INFO](/windows/win32/api/bthdef/ns-bthdef-bth_device_info) structure, which contains system-specific information, and a [**BTH_RADIO_INFO**](/windows-hardware/drivers/ddi/bthioctl/ns-bthioctl-_bth_radio_info) structure, which contains local radio-specific information.

To gather information about a specific remote Bluetooth device, a profile driver uses [**IOCTL_BTH_GET_RADIO_INFO**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_get_radio_info). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a BTH_RADIO_INFO structure that provides information about the specific remote radio, including whether the remote radio can be discovered and connected to.

To gather information about all remote radios that have been discovered, a profile driver uses [**IOCTL_BTH_GET_DEVICE_INFO**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_bth_get_device_info). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a [**BTH_DEVICE_INFO_LIST**](/windows-hardware/drivers/ddi/bthioctl/ns-bthioctl-_bth_device_info_list) structure that contains an array of BTH_DEVICE_INFO structures. The BTH_DEVICE_INFO_LIST structure contains one array entry for each discovered remote radio. The user-mode [BluetoothGetDeviceInfo](/windows/win32/api/bluetoothapis/nf-bluetoothapis-bluetoothgetdeviceinfo) API uses this functionality to return information about all remote radios.

To gather information about the remote device that caused the PnP Manager to load it, a profile driver uses [**IOCTL_INTERNAL_BTHENUM_GET_DEVINFO**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_internal_bthenum_get_devinfo). After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a BTH_DEVICE_INFO structure that contains information about the remote device, including its Bluetooth device address, device state, and its class-of-device (CoD) settings.

A profile driver uses [**IOCTL_INTERNAL_BTHENUM_GET_ENUMINFO**](/windows-hardware/drivers/ddi/bthioctl/ni-bthioctl-ioctl_internal_bthenum_get_enuminfo) to obtain information about the underlying device and service that caused the PnP manager to load the profile driver. After the IOCTL returns, its **AssociatedIrp.SystemBuffer** member contains a pointer to a [**BTH_ENUMERATOR_INFO**](/windows-hardware/drivers/ddi/bthddi/ns-bthddi-_bth_enumerator_info) structure that contains vendor-provided information about the device, including the port number, device flags, vendor ID, and product ID.

For more information about using Bluetooth IOCTLs and BRBs, see [Building and Sending a BRB](building-and-sending-a-brb.md).
