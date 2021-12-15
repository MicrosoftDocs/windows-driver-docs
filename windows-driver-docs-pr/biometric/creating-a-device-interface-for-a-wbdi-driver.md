---
title: Creating a Device Interface for a WBDI Driver
description: Creating a Device Interface for a WBDI Driver
keywords:
- biometric drivers WDK , device interfaces
- device interfaces WDK biometric
ms.date: 04/20/2017
---

# Creating a Device Interface for a WBDI Driver


After the device callback object has been initialized and returned to the driver, at the time of queue setup, the driver should create a device interface instance for the biometric device.

Specifically, WBDI drivers must expose the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface by calling [**IWDFDevice::CreateDeviceInterface**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-createdeviceinterface):

```cpp
hr = m_FxDevice->CreateDeviceInterface(&GUID_DEVINTERFACE_BIOMETRIC_READER, NULL);
```

This call is followed by a call to [**IWDFDevice::AssignDeviceInterfaceState**](/windows-hardware/drivers/ddi/wudfddi/nf-wudfddi-iwdfdevice-assigndeviceinterfacestate):

```cpp
hr = m_FxDevice->AssignDeviceInterfaceState(&GUID_DEVINTERFACE_BIOMETRIC_READER,
 NULL,
 TRUE);
```

A WBDI driver that wants to expose functionality to a legacy (non-WBDI) biometric stack should expose another device interface for legacy applications and make sure that the Exclusive value is set to zero in the INX file that installs the legacy stack.

Exposing the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface causes the WBF service to enumerate the driver only. If Exclusive mode is not set, WBF does not attempt to open and control the device.

Alternatively, the driver could detect internally that it is in legacy mode and then not expose the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface.

 

