---
title: Example 7 Stopping All Trace Sessions
description: Example 7 Stopping All Trace Sessions
ms.assetid: a832bf9a-ab7e-4ec0-823b-52bc6016e791
keywords: ["trace sessions WDK , stopping", "stopping trace sessions"]
---

# Example 7: Stopping All Trace Sessions


## <span id="ddk_stopping_all_trace_sessions_tools"></span><span id="DDK_STOPPING_ALL_TRACE_SESSIONS_TOOLS"></span>


The following command stops all trace sessions on the computer:

```
tracelog -x
```

In response, Tracelog lists each trace session running on the computer and asks if you want to stop the session. For example:

```
Do you want to stop the "My Trace" session (Y or N)?
```

To stop the session, type **Y**. Tracelog then lists the properties of the session along with the following message:

```
The "MyTrace" session has been stopped
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Example%207:%20Stopping%20All%20Trace%20Sessions%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




