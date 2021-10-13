---
title: Bluetooth Version and Profile Support in Previous Windows Versions
description: Bluetooth Version and Profile Support in Previous Windows Versions
ms.date: 09/14/2021
ms.localizationpriority: medium
---

# Bluetooth Version and Profile Support in Previous Windows Versions

> [!NOTE]
> Looking for drivers for your Bluetooth audio device? See [Fix connections to Bluetooth audio devices and wireless displays](https://go.microsoft.com/fwlink/p/?LinkID=623629).

> [!NOTE]
> For information about Bluetooth support in Windows 10, see [Bluetooth Support in Windows 10](general-bluetooth-support-in-windows.md).

## Which previous versions of Windows support Bluetooth wireless technology?

The following previous versions of Windows include in-box support for Bluetooth wireless technology:

* All SKUs of Windows 8.1
* All SKUs of Windows 8
* All SKUs of Windows 7
* All SKUs of Windows Vista
* All SKUs of Windows XP with Service Pack 2 (SP2) and later

> [!NOTE]
> The Windows XP with Service Pack 1 (SP1) release supported Bluetooth wireless technology, but did so with a driver that was available only to PC system partners. Windows XP with Service Pack 2 (SP2) integrated Bluetooth wireless technology support into a regular service pack release and was available to all customers.

The following previous versions of Windows **do not** have in-box support for Bluetooth wireless technology:

* All SKUs of Windows Server 2012
* All SKUs of Windows Server 2008 R2
* All SKUs of Windows Server 2008
* All SKUs of Windows Server 2003
* All SKUs of Windows 2000

Although these versions of Windows do not have in-box Bluetooth wireless technology support, third-party Bluetooth drivers might be available from independent hardware vendors (IHVs).

## Which Bluetooth versions do previous versions of Windows support?

Windows supports Bluetooth version 1.1 and later versions. Note that Bluetooth version 2.1 radios and devices are backward compatible with earlier versions of Bluetooth and will run on Windows XP and Windows Vista without SP2. However, these Windows versions cannot take advantage of the full Bluetooth version 2.1 feature set because the Bluetooth version 2.1 specification was not ratified before Windows Vista was released.

Windows 8 is Bluetooth Smart Ready, it supports Bluetooth version 4.0, and is able to connect with Bluetooth Smart devices.

Windows support for different versions of the Bluetooth specification depends on the Windows version, as shown in the following table:

| Windows version                         | Version 1.1 | Version 2.0 | Version 2.0 with EDR | Version 2.1 | Version 2.1 with EDR | Version 4.0 | Version 4.1 |
|-----------------------------------------|-------------|-------------|----------------------|-------------|----------------------|-------------|-------------|
| Windows 8.1                             | X           | X           | X                    | X           | X                    | X           |             |
| Windows 8                               | X           | X           | X                    | X           | X                    | X           |             |
| Windows 7                               | X           | X           | X                    | X           | X                    |             |             |
| Windows Vista with Service Pack 2 (SP2) | X           | X           | X                    | X           | X                    |             |             |
| Windows Vista with Service Pack 1 (SP1) | X           | X           | X                    | *           |                      |             |             |
| Windows Vista                           | X           | X           | X                    |             |                      |             |             |
| Windows XP                              | X           | X           | X                    |             |                      |             |             |

\* EDR support starting in Windows Vista and later is enhanced relative to the Bluetooth stack for Windows XP.

\*\* Windows Vista with SP1 supports Bluetooth version 2.1 if it includes a package that was made available only to system partners. Windows Vista with SP2 integrated the Bluetooth version 2.1 support into the service pack release so that it is available to all customers.

## What's new in Windows 8.1?

Windows 8.1 includes the following enhancements to the Bluetooth stack and related software:

* Inbox radio management control for Bluetooth version 4.0 radios.
* Windows Runtime API support for [**RFCOMM**](/uwp/api/Windows.Devices.Bluetooth.Rfcomm) and [**GATT**](/uwp/api/Windows.Devices.Bluetooth.GenericAttributeProfile) protocol access.

## What's new in Windows 8?

Windows 8 includes the following enhancements to the Bluetooth stack and related software:

* Support for Bluetooth version 4.0:
  * Bluetooth Low Energy support allows Windows to connect with Bluetooth Smart peripherals.
  * eL2CAP enables enhanced re-transmission and flow control for profiles that require this functionality.
* An extensible transport model allowing support for Bluetooth radios on non-USB buses
* Support for the HFP, A2DP, and AVRCP Profiles

## What is new in Windows 7?

Windows 7 includes the following enhancements to the Bluetooth stack and related software:

* Support for Bluetooth version 2.1:
  * Secure Simple Pairing allows Windows to determine the best pairing method to use between devices, rather than requiring users to make that determination.
  * Extended Inquiry Response enables sharing a device's friendly name much earlier in the pairing process.
* An improved user experience that enhances management of Bluetooth devices
* Improved installation of USB Bluetooth radios

Any USB device with a USB\\Class\_E0&SubClass\_01&Prot\_01 hardware ID will install as a *Generic Bluetooth Adapter*.

## What is new in Windows Vista?

Windows Vista includes the following enhancements to the Bluetooth stack and related software:

* Improved enhanced data rate (EDR) performance
* Adaptive frequency hopping (AFH). This feature improves the coexistence of Bluetooth radios and 802.11 (Wi-Fi) network adapters, both of which operate in the 2.4-GHz frequency range
* Synchronous connection-oriented (SCO) link support. This support is necessary for the headset and hands-free profiles
* Kernel-mode device driver interface (DDI) support for Logical Link Control and Adaptation Protocol (L2CAP), Service Discovery Protocol (SDP), and SCO.
* New Bluetooth hardware IDs, which are listed in the following table:

| Vendor identifier (VID) | Product identifier | Description                                       |
|-------------------------|--------------------|---------------------------------------------------|
| 03F0                    | 011D               | Hewlett Packard integrated Bluetooth module       |
| 03F0                    | 011D&Rev_0017      | Hewlett Packard nc4200                            |
| 03F0                    | 171D               | Hewlett Packard integrated Bluetooth module       |
| 03F0                    | D104               | BT450 Bluetooth wireless printer and PC adapter   |
| 044E                    | 300A               | Sony Bluetooth USB adapter                        |
| 044E                    | 300C               | Sony Bluetooth USB adapter                        |
| 049F                    | 0086               | Hewlett Packard integrated Bluetooth module       |
| 049F                    | 0086&Rev_1393      | Hewlett Packard nx7000                            |
| 0930                    | 0508               | Toshiba Bluetooth adapter                         |
| 0930                    | 0509               | Toshiba Bluetooth adapter                         |
| 0A5C                    | 201E               | IBM integrated Bluetooth IV                       |
| 0A5C                    | 2110               | ThinkPad Bluetooth with EDR                       |
| 0B05                    | 1712               | Generic Bluetooth adapter                         |
| 0DB0                    | 6855&Rev_2000      | Message signaled interrupt (MSI) Bluetooth device |
| 413C                    | 8120               | Dell wireless Bluetooth module                    |
| 413C                    | 8126               | Dell Truemobile 355 Bluetooth + EDR               |

## Which Bluetooth profiles have in-box support in previous versions of Windows?

### Windows 8.1 and Windows 8 In-Box Bluetooth Profiles

Because Windows 8.1, Windows 8, Windows 7, and Windows Vista provide both kernel-mode and user-mode programming interfaces for their Bluetooth stacks, hardware and software vendors can implement additional profiles in both kernel mode and user mode. We encourage vendors that create such profiles to test their software by using the appropriate [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) test suites and have their software packages digitally signed

### Windows 7 and Windows Vista In-Box Bluetooth Profiles

Windows 7 and Windows Vista include additional and updated Bluetooth profiles as listed in the following table:

| Profile   | Description                         |
|-----------|-------------------------------------|
| HID 1.1   | Human Interface Device              |
| PANU      | Personal Area Network User          |
| SPP       | Serial Port Profile                 |
| OPP       | Object Push Profile                 |
| DUN       | Dial-Up Networking                  |
| HCRP      | Hard Copy Replacement Profile       |
| HFP 1.5   | Hands-Free Profile                  |
| A2DP 1.2  | Advanced Audio Distribution Profile |
| AVRCP 1.3 | Audio/Video Remote Control Profile  |
| HOGP      | HID over GATT Profile               |

Windows included in-box support for the following Bluetooth profiles:

| Profile | Description                   |
|---------|-------------------------------|
| HID 1.0 | Human Interface Device        |
| PANU    | Personal Area Network User    |
| SPP     | Serial Port Profile           |
| OPP     | Object Push Profile           |
| DUN     | Dial-Up Networking            |
| HCRP    | Hard Copy Replacement Profile |

## Windows Phone 8 PICS report

The Profile/Protocol Implementation Conformance Statements (PICS) report for Windows Phone 8 is available from the Bluetooth SIG [PICS values](https://go.microsoft.com/fwlink/p/?LinkId=246801) webpage.

## Do users have to re-pair their Bluetooth devices after they upgrade a system to Windows 8.1?

If users upgrade from Windows 7 to Windows 8.1, they must perform a clean installation of Windows 8.1. In this situation, any Bluetooth software that the OEM provides must be re-installed and all devices must be re-paired. If users upgrade from Windows 8 to Windows 8.1, complex devices such as phones might require re pairing so that third-party drivers will reload. However, a simpler device such as a keyboard or a mouse does not require re-pairing.

Therefore, pairing information is preserved if users upgrade from Windows 8 to Windows 8.1 for some devices, primarily Bluetooth keyboards, mice, and audio devices. This ensures that customers are not required to use a wired keyboard and mouse to upgrade their Windows version. They can use their Bluetooth keyboard and mouse for the entire procedure.

## What programming interfaces were introduced in Windows 8.1?

Windows 8.1 introduces new Windows Runtime APIs for accessing the [**RFCOMM**](/uwp/api/Windows.Devices.Bluetooth.Rfcomm) (over standard Bluetooth) and [**GATT**](/uwp/api/Windows.Devices.Bluetooth.GenericAttributeProfile) (over Bluetooth Low Energy).

## What programming interfaces were introduced in Windows 8?

Windows 8 introduces new APIs for accessing Bluetooth Smart peripherals via Bluetooth Low Energy, creating a bus driver for non-USB Bluetooth controllers via an extensible transport model, and creating enhanced L2CAP channels. For more information about these APIs, see [Bluetooth Devices Reference](/windows/win32/api/_bltooth/).

## What programming interfaces were introduced in Windows 7?

Windows 7 introduced new Ex versions of previous APIs to provide enhanced functionality. For example, the BluetoothAuthenticateDeviceEx function lets out-of-band data be passed into the function call for the device that is being authenticated. Similarly, the [**BluetoothRegisterForAuthenticationEx**](/windows/win32/api/bluetoothapis/nf-bluetoothapis-bluetoothregisterforauthenticationex) function includes pin request and numeric comparison functionality. Also, the [**BluetoothSendAuthenticationResponseEx**](/windows/win32/api/bluetoothapis/nf-bluetoothapis-bluetoothsendauthenticationresponseex) function is called when an authentication request to send the numeric comparison response is received. For more information about the new Ex versions of these APIs, see [Bluetooth Functions](/windows/desktop/Bluetooth/bluetooth-functions).

## What programming interfaces were introduced in Windows Vista?

Windows Vista introduced a kernel-mode DDI for Bluetooth wireless technology, which provides access to SCO, SDP, and L2CAP. The DDI is included with Windows Driver Kit (WDK) build 6000, which was released with Windows Vista, and all later builds of the WDK. We do not intend to make the kernel-mode DDI available on earlier versions of Windows. The [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) can be used to verify that kernel-mode Bluetooth drivers comply with standard driver development practices and use the DDI correctly.

Windows Vista with SP2 and Windows 7 also support the user-mode RFComm and Bluetooth APIs. For more information, see the [Bluetooth design guide](./index.md). The WDK includes documentation for the new kernel-mode DDI. For more information about how to download the WDK, see [Other WDK downloads](../other-wdk-downloads.md) The HCK includes documentation for Driver Test Manager (DTM). For more information about how to download the HCK, see the [Windows Hardware Certification Kit (HCK)](https://go.microsoft.com/fwlink/p/?LinkId=733613) documentation.

## See also

* [Bluetooth Support in Windows 10](general-bluetooth-support-in-windows.md)
