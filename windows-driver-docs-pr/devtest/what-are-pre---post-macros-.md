---
title: What are PRE / POST macros
description: What are PRE / POST macros
ms.assetid: f5acb047-def3-443a-b220-77543f9a71e3
---

# What are PRE / POST macros?


PRE-logging and POST-logging macros define WPP\_LEVEL\_PRE(*level*) and WPP\_LEVEL\_POST(*level*) macros. The latter are user code that becomes part of the tracing function's expansion. PRE- and POST-logging macros can be used for any in-process setup or for cleanup around trace points.

By default they are set to do nothing. However, you can define them to add some pre-logging and post-logging logic.

```
PRE macro // If defined
If (WPP_CHECK_INIT && (Level,Flag) is enabled) {
....Call TraceMessage;
}
POST macro // If defined
```

For an example about how to define the PRE/POST macros, see [How are Trace-If expressions used?](how-are-trace-if-expressions-used-.md).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20What%20are%20PRE%20/%20POST%20macros?%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




