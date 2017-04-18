---
title: C28604
description: Warning C28604 Avoid calling SendMessageTimeout with SMTO\_ABORTIFHUNG with a timeout of 0.
ms.assetid: d9be9747-20f6-4a2b-a841-eaf3255f2f65
---

# C28604


warning C28604: Avoid calling SendMessageTimeout with SMTO\_ABORTIFHUNG with a timeout of 0

The Code Analysis tool reports this warning when applications call **SendMessageTimeout** with the **SMTO\_ABORTIFHUNG** flag and a time-out period of zero. Using **SendMessageTimeout** this way can be problematic because the time-out period has no effect, and the call is treated as a blocking call.

Specify a nonzero value for time-out period.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following function call can cause the process to not respond indefinitely.

```
fNeedsCallbackEvent = (0 != SendMessageTimeout(
_hwnd, 
WM_NULL, 
0,
0, 
SMTO_ABORTIFHUNG,
0,
&dwResult)); 
```

The following function call does not have this problem.

```
fNeedsCallbackEvent = (0 != SendMessageTimeout(
_hwnd, 
WM_NULL, 
0,
0,
SMTO_ABORTIFHUNG,
1000,  
&dwResult)); 
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28604%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




