---
title: Porting Issues Checklist
description: Porting Issues Checklist
ms.assetid: 6ab26321-85b8-4a5b-8ca5-af6cbf56ccd6
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Porting Issues Checklist





### General

-   Use the new 64-bit-safe Windows data types.

    The new 64-bit-safe data types, described earlier in this document, are defined in Basetsd.h. This header file is included in Ntdef.h, which is included in Ntddk.h, Wdm.h, and Ntifs.h.

-   Use the platform compiler macros carefully.

    The following assumption is no longer valid:

    ```cpp
    #ifdef _WIN32  // 32-bit Windows code
    ...
    #else          // 16-bit Windows code
    ...
    #endif
    ```

    However, the 64-bit compiler defines \_WIN32 for backward compatibility.

    Also, the following assumption is no longer valid:

    ```cpp
    #ifdef _WIN16  // 16-bit Windows code
    ...
    #else          // 32-bit Windows code
    ...
    #endif
    ```

    In this case, the else clause can represent \_WIN32 or \_WIN64.

-   Use the proper format specifiers with **printf** and **wsprintf**.

    Use **%p** to print pointers in hexadecimal. This is the best choice for printing pointers.

    **Note**   A future version of Visual C++ will support **%I** to print polymorphic data. It will treat values as 64 bits in 64-bit Windows and 32 bits in 32-bit Windows. Visual C++ will also support **%I64** to print values that are 64 bits.

     

<!-- -->

-   Know your address space.

    Do not blindly assume, for example, that if an address is a kernel address, its high-order bit must be set. To obtain the lowest system address, use the **MM\_LOWEST\_SYSTEM\_ADDRESS** macro.

### Pointer Arithmetic

-   Be careful when performing unsigned and signed operations.

    Consider the following:

    ```cpp
    ULONG x;
    LONG y;
    LONG *pVar1;
    LONG *pVar2;
     
    pVar2 = pVar1 + y * (x - 1);
    ```

    The problem arises because *x* is unsigned, which makes the entire expression unsigned. This works fine unless *y* is negative. In this case, *y* is converted to an unsigned value, the expression is evaluated using 32-bit precision, scaled, and added to *pVar1*. On 64-bit Windows, this 32-bit unsigned negative number becomes a large 64-bit positive number, which gives the wrong result. To fix this problem, declare *x* as a signed value or explicitly typecast it to **LONG** in the expression.

-   Be careful when using hexadecimal constants and unsigned values.

    The following assertion is not true on 64-bit systems:

    ```cpp
    ~((UINT64)(PAGE_SIZE-1)) == (UINT64)~(PAGE_SIZE-1)
    PAGE_SIZE = 0x1000UL  // Unsigned long - 32 bits
    PAGE_SIZE - 1 = 0x00000fff
    ```

    LHS expression:

    ```cpp
    // Unsigned expansion(UINT64)(PAGE_SIZE -1 ) = 0x0000000000000fff
    ~((UINT64)(PAGE_SIZE -1 )) = 0xfffffffffffff000
    ```

    RHS expression:

    ```cpp
    ~(PAGE_SIZE-1) = 0xfffff000
    (UINT64)(~(PAGE_SIZE - 1)) = 0x00000000fffff000
    ```

    Hence:

    ```cpp
    ~((UINT64)(PAGE_SIZE-1)) != (UINT64)(~(PAGE_SIZE-1))
    ```

-   Be careful with NOT operations.

    Consider the following:

    ```cpp
    UINT_PTR a; ULONG b;
    a = a & ~(b - 1); 
    ```

    The problem is that ~(b−1) produces 0x0000 0000 *xxxx xxxx* and not 0xFFFF FFFF *xxxx xxxx*. The compiler will not detect this. To fix this, change the code as follows:

    ```cpp
    a = a & ~((UINT_PTR)b - 1);
    ```

-   Be careful when computing buffer sizes.

    Consider the following:

    ```cpp
    len = ptr2 - ptr1 
    /* len could be greater than 2**32 */
    ```

    Cast pointers to **PCHAR** for pointer arithmetic.

    **Note**   If *len* is declared **INT** or **ULONG**, this will generate a compiler warning. Buffer sizes, even when computed correctly, may still exceed the capacity of **ULONG**.

     

-   Avoid using computed or hard-coded pointer offsets.

    When working with structures, use the [**FIELD\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff545727) macro wherever possible to determine the offset of structure members.

-   Avoid using hard-coded pointer or handle values.

    Do not pass hard-coded pointers or handles such as (HANDLE)0xFFFFFFFF to routines such as **ZwCreateSection**. Instead, use constants, such as INVALID\_HANDLE\_VALUE, that can be defined to have the appropriate value for each platform.

-   Be aware that in 64-bit Windows, 0xFFFFFFFF is not the same as -1.

    For example:

    ```cpp
    DWORD index = 0;
    CHAR *p;

    // if (p[index-1] == &#39;0&#39;) causes access violation on 64-bit Windows!
    ```

    On 32-bit machines:

    ```cpp
    p[index-1] == p[0xffffffff] == p[-1] 
    ```

    On 64-bit machines:

    ```cpp
    p[index-1] == p[0x00000000ffffffff] != p[-1]
    ```

    This problem can be avoided by changing the type of *index* from **DWORD** to **DWORD\_PTR**.

### Polymorphism

- Be careful with polymorphic interfaces.

  Do not create functions that accept parameters of type **DWORD** (or other fixed-precision types) for polymorphic data. If the data can be a pointer or an integral value, the parameter type should be **UINT\_PTR** or **PVOID**, not **DWORD**.

  For example, do not create a function that accepts an array of exception parameters typed as **DWORD** values. The array should be an array of **DWORD\_PTR** values. Therefore, the array elements can hold addresses or 32-bit integral values. The general rule is that if the original type is **DWORD** and it needs to be pointer width, convert it to a **DWORD\_PTR** value. That is why there are corresponding pointer-precision types for the native Win32 types. If you have code that uses **DWORD**, **ULONG**, or other 32-bit types in a polymorphic way (that is, you really want the parameter or structure member to hold an address), use **UINT\_PTR** in place of the current type.

- Be careful when calling functions that have pointer OUT parameters.

  Do not do this:

  ```cpp
  void GetBufferAddress(OUT PULONG *ptr);
  {
    *ptr=0x1000100010001000;
  }
  void foo()
  {
    ULONG bufAddress;
    //
    // This call causes memory corruption.
    //
    GetBufferAddress((PULONG *)&bufAddress);
  }
  ```

  Typecasting *bufAddress* to (**PULONG** \*) prevents a compiler error. However, *GetBufferAddress* will write a 64-bit value into the memory location at *&bufAddress*. Because *bufAddress* is only a 32-bit value, the 32 bits immediately following *bufAddress* will get overwritten. This is a very subtle, hard-to-find bug.

- Do not cast pointers to **INT**, **LONG**, **ULONG**, or **DWORD**.

  If you must cast a pointer to test some bits, set or clear bits, or otherwise manipulate its contents, use the **UINT**\_**PTR** or **INT**\_**PTR** type. These types are integral types that scale to the size of a pointer for both 32-bit and 64-bit Windows (for example, **ULONG** for 32-bit Windows and **\_int64** for 64-bit Windows). For example, assume you are porting the following code:

  ```cpp
  ImageBase = (PVOID)((ULONG)ImageBase | 1);
  ```

  As a part of the porting process, you would change the code as follows:

  ```cpp
  ImageBase = (PVOID)((ULONG_PTR)ImageBase | 1);
  ```

  Use **UINT**\_**PTR** and **INT**\_**PTR** where appropriate (and if you are uncertain whether they are required, there is no harm in using them just in case). Do not cast your pointers to the types **ULONG**, **LONG**, **INT**, **UINT**, or **DWORD**.

  **Note**  **HANDLE** is defined as a **void \\**<em>, so typecasting a **HANDLE</em>* value to a **ULONG** value to test, set, or clear the low two bits is a programming error.

     

- Use **PtrToLong** and **PtrToUlong** to truncate pointers.

  If you must truncate a pointer to a 32-bit value, use the **PtrToLong** or **PtrToUlong** function (defined in *Basetsd.h*). This function disables the pointer truncation warning for the duration of the call.

  Use these functions carefully. After you truncate a pointer variable using one of these functions, never cast the resulting **LONG** or **ULONG** back to a pointer. These functions truncate the upper 32 bits of an address, which are usually needed to access the memory originally referenced by pointer. Using these functions without careful consideration will result in fragile code.

### Data Structures and Structure Alignment

-   Carefully examine all uses of data structure pointers.

    The following are common trouble areas:

    -   Data structures that are stored on disk or exchanged with 32-bit processes.
    -   Explicit and implicit unions with pointers.
    -   Security descriptors.

<!-- -->

-   Use the [**FIELD\_OFFSET**](https://msdn.microsoft.com/library/windows/hardware/ff545727) macro.

    For example:

    ```cpp
    struct xx {
       DWORD NumberOfPointers;
       PVOID Pointers[1];
    };
     
    ```

    The following allocation is incorrect in 64-bit Windows because the compiler will pad the structure with an additional 4 bytes to make the 8-byte alignment requirement:

    ```cpp
    malloc(sizeof(DWORD)+100*sizeof(PVOID)); 
     
    ```

    Here is how to do it correctly:

    ```cpp
    malloc(FIELD_OFFSET(struct xx, Pointers) +100*sizeof(PVOID));
    ```

-   Use the **TYPE\_ALIGNMENT** macro.

    The **TYPE\_ALIGNMENT** macro returns the alignment requirement for a given data type on the current platform. For example:

    ```cpp
    TYPE_ALIGNMENT(KFLOATING_SAVE) == 4 on x86, 8 on Itanium
    TYPE_ALIGNMENT(UCHAR) == 1 everywhere
    ```

    As an example, code such as this:

    ```cpp
    ProbeForRead(UserBuffer, UserBufferLength, sizeof(ULONG));
    ```

    becomes more portable when changed to:

    ```cpp
    ProbeForRead(UserBuffer, UserBufferLength, TYPE_ALIGNMENT(ULONG));
    ```

-   Watch for data type changes in public kernel structures.

    For example, the **Information** field in the IO\_STATUS\_BLOCK structure is now of type **ULONG\_PTR**.

-   Be cautious when using structure packing directives.

    On 64-bit Windows, if a data structure is misaligned, routines that manipulate the structure, such as [**RtlCopyMemory**](https://msdn.microsoft.com/library/windows/hardware/ff561808) and **memcpy**, will not fault. Instead, they will raise an exception. For example:

    ```cpp
    #pragma pack (1)  /* also set by /Zp switch */
    struct Buffer {
        ULONG size;
        void *ptr;
    };

    void SetPointer(void *p) {
        struct Buffer s;
        s.ptr = p;  /* will cause alignment fault */
        ...
    }
    ```

    You could use the **UNALIGNED** macro to fix this:

    ```cpp
    void SetPointer(void *p) {
        struct Buffer s;
        *(UNALIGNED void *)&s.ptr = p;
    }
    ```

    Unfortunately, using the **UNALIGNED** macro is very expensive on Itanium-based processors. A better solution is to put 64-bit values and pointers at the beginning of the structure.

    **Note**  If possible, avoid using different packing levels in the same header file.

     

### Additional Information

-   [Supporting 32-Bit I/O in Your 64-Bit Driver](supporting-32-bit-i-o-in-your-64-bit-driver.md)

-   [Getting Ready for 64-bit Windows](https://msdn.microsoft.com/library/windows/desktop/aa384198) (user-mode application porting guide)

 

 




