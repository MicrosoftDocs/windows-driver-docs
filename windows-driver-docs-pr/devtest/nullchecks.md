---
title: NullCheck rule (storport)
description: The NullCheck rule verifies that a NULL value inside the driver code is not dereferenced later in the driver.
ms.assetid: 9322B5F8-6681-4000-A64C-E66D2D4A5D6D
ms.author: windowsdriverdev
ms.date: 05/21/2018
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: ["NullCheck rule (storport)"]
topic_type:
- apiref
api_name:
- NullCheck
api_type:
- NA
---

# NullCheck rule (storport)


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

|              |          |
|--------------|----------|
| Driver model | Storport |

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

 

 





