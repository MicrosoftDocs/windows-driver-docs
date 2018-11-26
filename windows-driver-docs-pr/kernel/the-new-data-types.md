---
title: The New Data Types
description: The New Data Types
ms.assetid: 13a0d51e-0a9a-471f-8427-d4a7a7eb6459
keywords: ["64-bit WDK kernel , porting drivers to", "porting drivers to 64-bit Windows", "data types WDK 64-bit", "fixed-precision integer types WDK 64-bit", "pointer-precision integer types WDK 64-bit", "specific-precision pointer types WDK 64-bit", "converting data types", "64-bit WDK kernel , data types"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# The New Data Types





There are three classes of new data types: fixed-precision integer types, pointer-precision integer types, and specific-precision pointer types. These types were added to the Windows environment (specifically, to Basetsd.h) to allow developers to prepare for 64-bit Windows well before its introduction. These new types were derived from the basic C-language integer and long types, so they work in existing code. Therefore, use these data types in your code now, test your code on 32-bit Windows, and use the 64-bit compiler to find and fix portability problems in advance, so your driver can be ready when 64-bit Windows is available for testing.

In addition, adopting these new data types will make your code more robust. To use these data types, you must scan your code for potentially unsafe pointer usage, polymorphism, and data definitions. To be safe, use the new types. For example, when a variable is of type **ULONG\_PTR**, it is clear that it will be used for casting pointers for arithmetic operations or polymorphism. It is not possible to indicate such usage directly by using the native Win32 data types. You can do this by using derived type naming or Hungarian notation, but both techniques are prone to errors.

### Fixed-Precision Integer Types

Fixed-precision data types are the same length for 32-bit and 64-bit programming. To help you remember this, their precision is part of the name of the data type. The following are the fixed-precision data types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DWORD32</strong></p></td>
<td><p>32-bit unsigned integer</p></td>
</tr>
<tr class="even">
<td><p><strong>DWORD64</strong></p></td>
<td><p>64-bit unsigned integer</p></td>
</tr>
<tr class="odd">
<td><p><strong>INT32</strong></p></td>
<td><p>32-bit signed integer</p></td>
</tr>
<tr class="even">
<td><p><strong>INT64</strong></p></td>
<td><p>64-bit signed integer</p></td>
</tr>
<tr class="odd">
<td><p><strong>LONG32</strong></p></td>
<td><p>32-bit signed integer</p></td>
</tr>
<tr class="even">
<td><p><strong>LONG64</strong></p></td>
<td><p>64-bit signed integer</p></td>
</tr>
<tr class="odd">
<td><p><strong>UINT32</strong></p></td>
<td><p>Unsigned <strong>INT32</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>UINT64</strong></p></td>
<td><p>Unsigned <strong>INT64</strong></p></td>
</tr>
<tr class="odd">
<td><p><strong>ULONG32</strong></p></td>
<td><p>Unsigned <strong>LONG32</strong></p></td>
</tr>
<tr class="even">
<td><p><strong>ULONG64</strong></p></td>
<td><p>Unsigned <strong>LONG64</strong></p></td>
</tr>
</tbody>
</table>

 

### Pointer-Precision Integer Types

As the pointer precision changes (that is, as it becomes 32 bits when compiled for 32-bit platforms, 64 bits when compiled for 64-bit platforms), these data types reflect the precision accordingly. Therefore, it is safe to cast a pointer to one of these types when performing pointer arithmetic; if the pointer precision is 64 bits, the type is 64 bits. The count types also reflect the maximum size to which a pointer can refer. The following are the pointer-precision and count types.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DWORD_PTR</strong></p></td>
<td><p>Unsigned long type for pointer precision.</p></td>
</tr>
<tr class="even">
<td><p><strong>HALF_PTR</strong></p></td>
<td><p>Signed integral type for half-pointer precision (16 bits on 32-bit systems, 32 bits on 64-bit systems).</p></td>
</tr>
<tr class="odd">
<td><p><strong>INT_PTR</strong></p></td>
<td><p>Signed integral type for pointer precision.</p></td>
</tr>
<tr class="even">
<td><p><strong>LONG_PTR</strong></p></td>
<td><p>Signed long type for pointer precision.</p></td>
</tr>
<tr class="odd">
<td><p><strong>SIZE_T</strong></p></td>
<td><p>The maximum number of bytes to which a pointer can refer. Use this type for a count that must span the full range of a pointer.</p></td>
</tr>
<tr class="even">
<td><p><strong>SSIZE_T</strong></p></td>
<td><p>Signed <strong>SIZE_T</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>UHALF_PTR</strong></p></td>
<td><p>Unsigned <strong>HALF_PTR</strong>.</p></td>
</tr>
<tr class="even">
<td><p><strong>UINT_PTR</strong></p></td>
<td><p>Unsigned <strong>INT_PTR</strong>.</p></td>
</tr>
<tr class="odd">
<td><p><strong>ULONG_PTR</strong></p></td>
<td><p>Unsigned <strong>LONG_PTR</strong>.</p></td>
</tr>
</tbody>
</table>

 

### Fixed-Precision Pointer Types

There are also new pointer types that explicitly size the pointer. Be cautious when using these pointer types in 64-bit code: If you declare the pointer using a 32-bit type, the system creates the pointer by truncating a 64-bit pointer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Type</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>POINTER_32</strong></p></td>
<td><p>A 32-bit pointer. On a 32-bit system, this is a native pointer. On a 64-bit system, this is a truncated 64-bit pointer.</p></td>
</tr>
<tr class="even">
<td><p><strong>POINTER_64</strong></p></td>
<td><p>A 64-bit pointer. On a 64-bit system, this is a native pointer. On a 32-bit system, this is a sign-extended 32-bit pointer.</p>
<p>Note that it is not safe to assume the state of the high pointer bit.</p></td>
</tr>
</tbody>
</table>

 

### Helper Functions

The following inline functions (defined in Basetsd.h) can help you safely convert values from one type to another:

```cpp
unsigned long HandleToUlong( const void *h )
long HandleToLong( const void *h )
void * LongToHandle( const long h )
unsigned long PtrToUlong( const void *p )
unsigned int PtrToUint( const void *p )
unsigned short PtrToUshort( const void *p )
long PtrToLong( const void *p )
int PtrToInt( const void *p )
short PtrToShort( const void *p )
void * IntToPtr( const int i )
void * UIntToPtr( const unsigned int ui )
void * LongToPtr( const long l )
void * ULongToPtr( const unsigned long ul )
```

**Warning**  **IntToPtr** sign-extends the **int** value, **UIntToPtr** zero-extends the unsigned **int** value, **LongToPtr** sign-extends the **long** value, and **ULongToPtr** zero-extends the **unsigned long** value.

 

 

 




