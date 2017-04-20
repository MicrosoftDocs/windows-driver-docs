---
title: TDR Registry Keys
description: TDR Registry Keys
ms.assetid: 77b8b2aa-0821-4297-a1e4-57894bd4181f
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# TDR Registry Keys


You can use the following TDR-related registry keys for testing or debugging purposes only. That is, they should not be manipulated by any applications outside targeted testing or debugging.

-   **TdrLevel**

    Specifies the initial level of recovery. The default value is to recover on timeout (**TdrLevelRecover**).

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrLevel
    ValueType : REG_DWORD
    ValueData : TdrLevelOff (0) - Detection disabled 
     TdrLevelBugcheck (1) - Bug check on detected timeout, for example, no recovery.
     TdrLevelRecoverVGA (2) - Recover to VGA (not implemented).
     TdrLevelRecover (3) - Recover on timeout. This is the default value.
    ```

-   **TdrDelay**

    Specifies the number of seconds that the GPU can delay the preempt request from the GPU scheduler. This is effectively the timeout threshold. The default value is 2 seconds.

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrDelay
    ValueType : REG_DWORD
    ValueData : Number of seconds to delay. 2 seconds is the default value.
    ```

-   **TdrDdiDelay**

    Specifies the number of seconds that the operating system allows threads to leave the driver. After a specified time, the operating system bug-checks the computer with the code VIDEO\_TDR\_FAILURE (0x116). The default value is 5 seconds.

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrDdiDelay
    ValueType : REG_DWORD
    ValueData : Number of seconds to leave the driver. 5 seconds is the default value.
    ```

-   **TdrTestMode**

    Reserved. Do not use.

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrTestMode
    ValueType : REG_DWORD
    ValueData : Do not use.
    ```

-   **TdrDebugMode**

    Specifies the debugging-related behavior of the TDR process. The default value is TDR\_DEBUG\_MODE\_RECOVER\_NO\_PROMPT, which indicates not to break into the debugger.

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrDebugMode
    ValueType : REG_DWORD
    ValueData : TDR_DEBUG_MODE_OFF (0) - Break to kernel debugger before the recovery to allow investigation of the timeout. 
     TDR_DEBUG_MODE_IGNORE_TIMEOUT (1) - Ignore any timeout.
     TDR_DEBUG_MODE_RECOVER_NO_PROMPT (2) - Recover without breaking into the debugger. This is the default value.
     TDR_DEBUG_MODE_RECOVER_UNCONDITIONAL (3) - Recover even if some recovery conditions are not met (for example, recover on consecutive timeouts).
    ```

-   **TdrLimitTime**

    Supported in Windows Server 2008 and later versions, and Windows Vista with Service Pack 1 (SP1) and later versions.

    Specifies the default time within which a specific number of TDRs (specified by the **TdrLimitCount** key) are allowed without crashing the computer. The default value is 60 seconds.

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrLimitTime
    ValueType : REG_DWORD
    ValueData : Number of seconds before crashing. 60 seconds is the default value.
    ```

-   **TdrLimitCount**

    Supported in Windows Server 2008 and later versions, and Windows Vista with Service Pack 1 (SP1) and later versions.

    Specifies the default number of TDRs (0x117) that are allowed during the time specified by the **TdrLimitTime** key without crashing the computer. The default value is 5.

    ```
    KeyPath   : HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\GraphicsDrivers
    KeyValue  : TdrLimitCount
    ValueType : REG_DWORD
    ValueData : Number of TDRs before crashing. The default value is 5.
    ```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20TDR%20Registry%20Keys%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




