---
title: C28170
description: Warning C28170 The function has been declared to be in a paged segment, but neither PAGED\_CODE nor PAGED\_CODE\_LOCKED was found.
ms.assetid: 9efffcc8-54b6-46f8-b037-53c66a8eace2
keywords: ["warnings listed WDK PREfast for Drivers", "errors listed WDK PREfast for Drivers"]
---

# C28170


warning C28170: The function has been declared to be in a paged segment, but neither PAGED\_CODE nor PAGED\_CODE\_LOCKED was found

The Code Analysis tool reports this error when **\#pragma alloc\_text** or **\#pragma code\_seg** is used to move a function that does not contain a PAGED\_CODE or PAGED\_CODE\_LOCKED macro into a pageable code section. This error is reported at the line number that corresponds to the first brace (**{**) in the function.

The Code Analysis tool infers that a section is pageable when the section name begins with PAGE. The functions in pageable code must contain a PAGED\_CODE or PAGED\_CODE\_LOCKED macro at the beginning of the function between the first brace (**{** ) and the first conditional statement.

These macros allow the Code Analysis tool and a run-time checker to determine whether pageable code might be run at an elevated IRQL. If a page fault occurs while the system is running at an elevated level, the system will crash.

If the functions in a paged segment are subsequently locked into memory, use PAGED\_CODE\_LOCKED instead of PAGED\_CODE. The PAGE\_CODE\_LOCKED macro permits the driver to make calls that raise the IRQL without encountering a PREfast for Drivers warning.

This condition is often very difficult to find while testing (unless the PAGED\_CODE macro is used to cause the Driver Verifier to check for the error), because the code must actually be paged out for the page fault to occur.

### <span id="example"></span><span id="EXAMPLE"></span>Example

The following code example elicits this warning.

```
void func();
#pragma alloc_text("PAGED_CODE", func);

void func1()
{
   // paged, no PAGED_CODE: error
}
```

The following code example avoids this warning.

```
void func();
#pragma alloc_text("PAGED_CODE", func);

void func2()
{
   PAGED_CODE(); // includes PAGED_CODE macro
}
```

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20C28170%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




