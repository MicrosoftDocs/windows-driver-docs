---
title: Static Driver Verifier General Tool and Technical Limitations
description: Static Driver Verifier General Tool and Technical Limitations
ms.assetid: d263dee5-2408-4772-96d7-d1895a445fab
keywords:
- Static Driver Verifier WDK , limitations
- StaticDV WDK , limitations
- SDV WDK , limitations
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Static Driver Verifier General Tool and Technical Limitations


SDV has the following general limitations:

-   SDV verifies only one driver at a time and the driver must follow one of these driver models to be fully verified: WDM, KMDF, NDIS, or Storport. For more information about the supported drivers, see [Determining if Static Driver Verifier supports your driver or library](determining-if-static-driver-verifier-supports-your-driver-or-library.md).

-   Drivers that do not fall into one of the above categories will be severely limited in the rules that can be verified and are more likely to fail during analysis.

-   The driver project file and source code must reside on the local computer. You cannot verify drivers remotely.

-   SDV is installed with the English (United States) locale. As a result, locale-dependent elements, such as string formatting, use the English (United States) variants. This limitation is present even when SDV is installed on localized versions of Windows other than English (United States).

The SDV [verification engine](verification-engine.md) has technical limitations that prevent it from correctly interpreting some driver code. Specifically, the verification engine:

-   Does not recognize that 32-bit integers are limited to 32 bits. As a result, it does not detect overflow or underflow errors.

-   Makes sure that drivers that declare their entry points with the **static** keyword are processed correctly. However, to ensure that static entry points are recognized, SDV required a change to the [Sdv-map.h](sdv-map-h.md) files for static functions: For example, if you declare a static entry point:

    ```
    static DRIVER_UNLOAD Unload;
    ```

    The Sdv-map.h will not contain the usual entry for *fun\_DriverUnload*.

    ```
    #define fun_DriverUnload Unload
    ```

    Instead, you see that the function name is mangled:

    ```
      #define fun_DriverUnload sdv_static_function_Unload_1
    ```

    This is necessary as multiple modules might have a static function named *Unload*. The name is mangled to avoid potential conflicts.

-   Cannot interpret driver dispatch or driver callback functions that are defined in an export driver where the export driver has a module-definition (.def) file that hides the driver dispatch function. To avoid this issue, add the driver dispatch function to the EXPORTS section of the module-definition (.def) file.

-   Cannot successfully detect the role type of a function if the following references to this function are in not in the same *compilation unit*.

    -   Declaration of the function.
    -   Definition of the function.
    -   Assignment of the function to a driver entry point or callback function.

    The *compilation unit* is defined here as the smallest set of source code files and other source files included by this source code file.

    If a function role type is not detected by SDV, SDV will not verify the traces that originate from this function.

    For example, if a driver defines (or implements) an [*EvtDriverDeviceAdd*](https://msdn.microsoft.com/library/windows/hardware/ff541693) function in the file mydriver.c. This compilation unit (or any .h files that mydriver.c includes) must contain the function role type declaration for the *EvtDriverDeviceAdd* function.

-   Does not interpret structured exception handling. For **try/except** statements, SDV analyzes the guarded section as if no exception is thrown. Does not analyze the expression or the exception handler code.

    ```
    // The try/except statement
    __try 
    {
       // guarded section
    }
    __except ( expression )
    {
       // exception handler
    } 
    ```

    For **try/finally** statements, SDV analyzes the guarded section and then the termination handler, as if no exception is thrown.

    ```
    // The try/finally statement
    __try {
       // guarded section
    }
    __finally {
       // termination handler
    }
    ```

    For both **try/except** and **try/finally** statements, SDV ignores the **leave** statement.

    For both **try/except** and **try/finally** statements, a jump out of the **try** block prevents analysis of the **except** or **finally** statements. For information about how to rewrite so that you can use a leave statement, see the topic for compiler warning [C6242](http://go.microsoft.com/fwlink/p/?linkid=153317).

-   Ignores pointer arithmetic. For example, it will miss situations in which a pointer is incremented or decremented. This limitation can result in false negative and false positive results.

-   Ignores unions. In most circumstances a **union** is treated as a **struct** and this could result in false positives or false negatives.

-   Ignores casting operations, so it will miss both errors that are solved by recasting and errors that are caused by casting. For example, the engine assumes that an integer that is recast as a character still has the integer value.

-   Only initializes arrays that are function pointer arrays. SDV issues a warning and compresses the array initializer to the first 1000 elements. For other array types, only the first element is initialized.

-   Constructors of objects that are initialized in arrays are not called. For example, in the following code snippet, *x* does not get set to 10 because SDV does not call the constructor.

    ```
    class A
    {
    public:
        A() {
          x = 10;
        }

        int x;
    };

    void main()
    {
        A a[1];
    }
    ```

-   SDV does not support the use of constructors to initialize arrays. For example, in the following code snippet, the constructor for P will not be called correctly in the main function and will not initialize the element in array p2:
    ```
    class P
    {
    public:
        P() : x(0) {}
        int x;
    };

    void main()
    {
        P* p1 = new P[1];

        P p2[1] = {P()};
    }
    ```

-   SDV ignores precompiled headers. Drivers that use precompiled headers solely for speeding up compilation will compile slower with SDV. Drivers that must use precompiled headers for successful compilation will not compile with SDV.

-   Cannot infer some types of implicit assignments that are made through calls to **RtlZeroMemory** or **NdisZeroMemory**. The engine does a best-effort analysis to initialize the memory to zero, but only when it can identify its type. As a result, code that depends upon these functions to initialize memory could yield false defects along some code paths.

-   Does not support a memory model that would allow it to track the manual dispatching of I/O requests to a KMDF driver. The engine only supports methods that rely on the framework to deliver the I/O requests to the driver (for sequential or parallel dispatching).

-   Does not support the use of the float data type for comparisons. This technical limitation can yield false negative and false positive results.

-   SDV does not support virtual inheritance or virtual functions. SDV does not generate defects that follow a code path through virtual functions, which might lead to lost true defects. Virtual inheritance is treated like regular inheritance, which might lead to false defects or lost true defects.

 

 





