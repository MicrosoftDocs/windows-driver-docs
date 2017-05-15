---
title: ndiskd.ndis
description: The ndiskd.ndis extension displays build information about ndis.sys.
ms.assetid: d852d6cc-7eba-4dad-aba5-3a2c9eac2f46
keywords: ["ndiskd.ndis Windows Debugging"]
topic_type:
- apiref
api_name:
- ndiskd.ndis
api_type:
- NA
---

# !ndiskd.ndis


The **!ndiskd.ndis** extension displays build information about ndis.sys.

``` syntax
    !ndiskd.ndis 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


This extension has no parameters.

### <span id="DLL"></span><span id="dll"></span>DLL

Ndiskd.dll

Examples
--------

The following example shows that the debugee machine has a Checked Ndis build.

```cmd
0: kd> !ndiskd.ndis
Checked Ndis
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[debugger\debugger]:%20!ndiskd.ndis%20%20RELEASE:%20%285/15/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




