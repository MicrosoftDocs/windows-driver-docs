---
title: C28129
description: Warning C28129 An assignment has been made to an operand, which should only be modified using bit sets and clears.
ms.assetid: b5afad45-6498-42f3-b1aa-9ba3cc8abb6d
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28129


warning C28129: An assignment has been made to an operand, which should only be modified using bit sets and clears

The driver is using an assignment to modify an operand. Assigning a value might unintentionally change the values of bits other than those that it needs to change, resulting in unexpected consequences.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
fdo->Flags = DO_BUFFERED_IO;
```

The following code example avoids this warning.

```
fdo->Flags |= DO_BUFFERED_IO;
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28129%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




