---
title: Dealing with Unavailable Symbol Stores
description: Dealing with Unavailable Symbol Stores
ms.assetid: 42e3518b-b139-49cd-96cc-ea31f6df7964
keywords: ["SymProxy, unavailable stores"]
---

# Dealing with Unavailable Symbol Stores


If one of the symbol stores that SymSrv is configured to obtain files from is down or otherwise unavailable, the result can be long waits from the client for every file request. When SymSrv is called from SymProxy, you can avoid most of these waits by setting up SymSrv to stop trying to access the store in question. When this feature is engaged, SymSrv stops trying to use the store for a set period of time after it experiences a specified number of timeouts from the same store during a set interval. The values of these variables can be controlled either by an .ini file or from the registry.

**To control symbol store access using a .ini file**

1.  In %WINDIR%\\system32\\inetsrv\\Symsrv.ini, create a section called **timeouts**.

2.  Add the values **trigger**, **count**, and **blackout** to this section.

**Trigger** indicates the amount of time in minutes to watch for timeouts. **Count** indicates the number of timeouts to look for during the **trigger** period. **Blackout** indicates the length of time in minutes to disable the store after the threshhold is reached.

For example, we recommend the following settings:

```
[timeouts]
trigger=10
count=5
blackout=15
```

In this example, the store access is turned off if five timeouts are experienced in a 10-minute period. At the completion of a 15-minute blackout, the store is reactivated.

**To control symbol store access using the registry**

1.  Create a key named
    ```
    HKLM\ Software\Microsoft\Symbol Server\Timeouts
    ```

2.  Add three REG\_DWORD values **trigger**, **count**, and **blackout** to this key. Set these values as you would in the .ini file.

Whether using the registry or an .ini file, if any of the trigger, count, or blackout values are set to 0 or if any of the keys or values do not exist, this functionality is disabled.

This feature of SymSrv is currently available only when running as a service. This means that the only practical application of this feature is when it is called from SymProxy.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20Dealing%20with%20Unavailable%20Symbol%20Stores%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




