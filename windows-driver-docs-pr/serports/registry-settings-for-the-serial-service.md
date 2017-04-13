---
title: Registry Settings for the Serial Service
author: windows-driver-content
description: Registry Settings for the Serial Service
ms.assetid: 5c4a28ab-e2e5-45b4-8179-6f5d40e9c98c
keywords: ["Serial service WDK"]
---

# Registry Settings for the Serial Service


## <a href="" id="ddk-registry-settings-for-the-serial-service-kg"></a>


This topic describes the registry settings that Serial applies to all serial devices for which Serial is the function driver or a lower-level device filter driver.

Serial queries the service entry values after it is loaded. If an entry value is not present, Serial adds the service entry value. Serial sets the entry value to the default value that is statically defined in the system-supplied Serial.sys driver. If a service entry value is changed after Serial is loaded, the new value is used the next time Serial is loaded.

Serial uses the following service entry values that are under the **..\\Services\\Serial** registry key:

<a href="" id="forcefifoenable--reg-dword-"></a>**ForceFifoEnable** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether to force Serial to use FIFOs. If **ForceFifofEnable** is nonzero, FIFOs are used, regardless of whether Serial can detect the presence of FIFOs. Otherwise, FIFOs are used only if Serial can detect them. The default value of is nonzero. If the entry value is not present, Serial sets a **ForceFifoEnable** entry value to the default value. For more information about the method of detection, see the [Serial driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617962) on GitHub.

<a href="" id="rxfifo--reg-dword-"></a>**RxFIFO** (REG\_DWORD)  
Specifies the number of bytes in the receive FIFO that triggers a port interrupt. For valid values, see the constants defined in the Serial.h header file in the [Serial driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617962) on GitHub. The default value of **RxFIFO** is eight bytes. If the entry value is not present, Serial sets an **RxFIFO** entry value to the default value.

<a href="" id="txfifo--reg-dword-"></a>**TxFIFO** (REG\_DWORD)  
Specifies the number of bytes in the transmit FIFO that triggers a port interrupt. For valid values, see the constants defined in the Serial.h header file in the [Serial driver sample](http://go.microsoft.com/fwlink/p/?LinkId=617962) on GitHub. The default value of **TxFIFO** is 14 bytes. If the entry value is not present, Serial sets a **TxFIFO** entry value to the default value.

<a href="" id="permitshare--reg-dword-"></a>**PermitShare** (REG\_DWORD)  
Specifies a Boolean flag that indicates whether to permit the system to share the interrupt that a port uses. If **PermitShare** is nonzero, the interrupt can be shared; otherwise, the interrupt cannot be shared. The default value of **PermitShare** is 0x00000000. If the entry value is not present, Serial sets a **PermitShare** entry value to the default value.

<a href="" id="breakonentry--debuglevel--and-logfifo"></a>**BreakOnEntry**, **DebugLevel**, and **LogFifo**  
Specify entry values that are used for debugging. For more information about these entry values, see the Serial sample code that is included in the WDK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bserports\serports%5D:%20Registry%20Settings%20for%20the%20Serial%20Service%20%20RELEASE:%20%288/4/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


