---
title: Creating a Device Interface for a WBDI Driver
description: Creating a Device Interface for a WBDI Driver
ms.assetid: 8595092c-9105-4638-814a-74cdfa372638
keywords: ["biometric drivers WDK , device interfaces", "device interfaces WDK biometric"]
---

# Creating a Device Interface for a WBDI Driver


After the device callback object has been initialized and returned to the driver, at the time of queue setup, the driver should create a device interface instance for the biometric device.

Specifically, WBDI drivers must expose the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface by calling [**IWDFDevice::CreateDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff557016):

```
hr = m_FxDevice->CreateDeviceInterface(&GUID_DEVINTERFACE_BIOMETRIC_READER, NULL);
```

This call is followed by a call to [**IWDFDevice::AssignDeviceInterfaceState**](https://msdn.microsoft.com/library/windows/hardware/ff557006):

```
hr = m_FxDevice->AssignDeviceInterfaceState(&GUID_DEVINTERFACE_BIOMETRIC_READER,
 NULL,
 TRUE);
```

A WBDI driver that wants to expose functionality to a legacy (non-WBDI) biometric stack should expose another device interface for legacy applications and make sure that the Exclusive value is set to zero in the INX file that installs the legacy stack.

Exposing the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface causes the WBF service to enumerate the driver only. If Exclusive mode is not set, WBF does not attempt to open and control the device.

Alternatively, the driver could detect internally that it is in legacy mode and then not expose the GUID\_DEVINTERFACE\_BIOMETRIC\_READER device interface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[biometric\biometric]:%20Creating%20a%20Device%20Interface%20for%20a%20WBDI%20Driver%20%20RELEASE:%20%288/24/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




