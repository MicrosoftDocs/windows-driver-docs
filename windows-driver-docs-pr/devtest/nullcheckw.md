---
title: NullCheck rule (wdm)
description: The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver.
ms.assetid: 840906B2-E6D4-4BC8-AC38-461824B70BFA
keywords: ["NullCheck rule (wdm)"]
topic_type:
- apiref
api_name:
- NullCheck
api_type:
- NA
---

# NullCheck rule (wdm)


The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver. This rule reports a defect if either of these conditions is true:

-   There is an assignment of NULL that is dereferenced later.
-   There is a global/parameter to a procedure in a driver that may be NULL that is dereferenced later, and there is an explicit check in the driver that suggests that the initial value of the pointer may be NULL.

With NullCheck rule violations, the most relevant code statements are highlighted in the trace tree pane. For more information about working with report output, see [Static Driver Verifier Report](https://msdn.microsoft.com/library/windows/hardware/ff552834) and [Understanding the Trace Viewer](https://msdn.microsoft.com/library/windows/hardware/ff554020).

**Struct Example**

This code snippet shows the proper use of a structure.

```
//Rule does not fail
typedef struct _B { 
    int *f; 
} B;
void GoodStruc(B *x) {
    B *y = x;
    y->f = NULL; //assign NULL
    if (x->f) {
        *(x->f) = 1;
    } //OK
    
}
```

This code snippet shows the improper use of a structure. The code will compile, but will produce a runtime error.

```
//Rule fails
typedef struct _A {
    int *f; 
} A;

void BadStruc(A *x) {
    A *y = x;
    y->f = NULL; //assign NULL
    *(x->f) = 1; //dereferencing NULL
}
```

**Function Example**

In this example, there is a parameter to a function that may be NULL, that is dereferenced later. In addition, there is an explicit check that suggests that the initial value of the pointer may be NULL.

```
//Rule fails
void Bad(int *x)
{
    *x = 2; //Possibly dereferencing NULL
    if (x != NULL) //checks for null on a parameter
        *x = *x + 1;
}
```

In this example, there is no rule violation since there is likely an implicit precondition that the parameter is not expected to be NULL.

```
//Rule does not fail
void Good1(int *x)
{
     *x = 2;
     *x = *x + 1;
}
```

In this second example, there is an explicit check for NULL, each time the parameter is used.

```
//Rule does not fail
void Good2(int *x)
{
    if (x != NULL)
        *x = 2; // ok
    if (x != NULL) //checks for null on a parameter
        *x = *x + 1;
}
```

|              |     |
|--------------|-----|
| Driver model | WDM |

How to test
-----------

<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">At compile time</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Run [Static Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff552808) and specify the <strong>NullCheck</strong> rule.</p>
Use the following steps to run an analysis of your code:
<ol>
<li>[Prepare your code (use role type declarations).](https://msdn.microsoft.com/library/windows/hardware/hh454281#preparing-your-source-code)</li>
<li>[Run Static Driver Verifier.](https://msdn.microsoft.com/library/windows/hardware/hh454281#running-static-driver-verifier)</li>
<li>[View and analyze the results.](https://msdn.microsoft.com/library/windows/hardware/hh454281#viewing-and-analyzing-the-results)</li>
</ol>
<p>For more information, see [Using Static Driver Verifier to Find Defects in Drivers](https://msdn.microsoft.com/library/windows/hardware/hh454281).</p></td>
</tr>
</tbody>
</table>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bdevtest\devtest%5D:%20NullCheck%20rule%20%28wdm%29%20%20RELEASE:%20%281/17/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




