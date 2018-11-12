---
title: Converting Virtual Addresses to Physical Addresses
description: Converting Virtual Addresses to Physical Addresses
ms.assetid: 5b3d19df-09cc-4131-ae64-5ce64d986df3
keywords: ["virtual address", "virtual address, converting to physical address", "physical address", "physical address, converting from virtual address", "addresses", "addresses, converting virtual to physical", "memory, virtual addresses", "memory, physical addresses"]
ms.author: domars
ms.date: 05/04/2018
ms.localizationpriority: medium
---

# Converting Virtual Addresses to Physical Addresses

## <span id="ddk_converting_virtual_addresses_to_physical_addresses_dbg"></span><span id="DDK_CONVERTING_VIRTUAL_ADDRESSES_TO_PHYSICAL_ADDRESSES_DBG"></span>


Most debugger commands use virtual addresses, not physical addresses, as their input and output. However, there are times that having the physical address can be useful.

There are two ways to convert a virtual address to a physical address: by using the **!vtop** extension, and by using the **!pte** extension.

For an overview of virtual address in Windows, see [Virtual address spaces](https://docs.microsoft.com/windows-hardware/drivers/gettingstarted/virtual-address-spaces). 


### <span id="address_conversion_using__vtop"></span><span id="ADDRESS_CONVERSION_USING__VTOP"></span>Address Conversion Using !vtop

Suppose you are debugging a target computer on which the MyApp.exe process is running and you want to investigate the virtual address 0x0012F980. Here is the procedure you would use with the **!vtop** extension to determine the corresponding physical address.

**Converting a virtual address to a physical address using !vtop**

1.  Make sure that you are working in hexadecimal. If necessary, set the current base with the [**N 16**](n--set-number-base-.md) command.

2.  Determine the *byte index* of the address. This number is equal to the lowest 12 bits of the virtual address. Thus, the virtual address 0x0012F980 has a byte index of 0x980.

3.  Determine the *directory base* of the address by using the [**!process**](-process.md) extension:

    ```dbgcmd
    kd> !process 0 0
    **** NT ACTIVE PROCESS DUMP ****
    ....
    PROCESS ff779190  SessionId: 0  Cid: 04fc    Peb: 7ffdf000  ParentCid: 0394
     DirBase: 098fd000  ObjectTable: e1646b30  TableSize:   8.
        Image: MyApp.exe
    ```

4.  Determine the *page frame number* of the directory base. This is simply the directory base without the three trailing hexadecimal zeros. In this example, the directory base is 0x098FD000, so the page frame number is 0x098FD.

5.  Use the [**!vtop**](-vtop.md) extension. The first parameter of this extension should be the page frame number. The second parameter of **!vtop** should be the virtual address in question:

    ```dbgcmd
    kd> !vtop 98fd 12f980
    Pdi 0 Pti 12f
    0012f980 09de9000 pfn(09de9)
    ```

    The second number shown on the final line is the physical address of the beginning of the physical page.

6.  Add the byte index to the address of the beginning of the page: 0x09DE9000 + 0x980 = 0x09DE9980. This is the desired physical address.

You can verify that this computation was done correctly by displaying the memory at each address. The [**!d\\***](-db---dc---dd---dp---dq---du---dw.md) extension displays memory at a specified physical address:

```dbgcmd
kd> !dc 9de9980
# 9de9980 6d206e49 726f6d65 00120079 0012f9f4 In memory.......
# 9de9990 0012f9f8 77e57119 77e8e618 ffffffff .....q.w...w....
# 9de99a0 77e727e0 77f6f13e 77f747e0 ffffffff .'.w>..w.G.w....
# 9de99b0 .....
```

The [**d\* (Display Memory)**](d--da--db--dc--dd--dd--df--dp--dq--du--dw--dw--dyb--dyd--display-memor.md) command uses a virtual address as its argument:

```dbgcmd
kd> dc 12f980
0012f980  6d206e49 726f6d65 00120079 0012f9f4  In memory.......
0012f990  0012f9f8 77e57119 77e8e618 ffffffff  .....q.w...w....
0012f9a0  77e727e0 77f6f13e 77f747e0 ffffffff  .'.w>..w.G.w....
0012f9b0  .....
```

Because the results are the same, this indicates that the physical address 0x09DE9980 does indeed correspond to the virtual address 0x0012F980.

### <span id="address_conversion_using__pte"></span><span id="ADDRESS_CONVERSION_USING__PTE"></span>Address Conversion Using !pte

Again, assume you are investigating the virtual address 0x0012F980 belonging to the MyApp.exe process. Here is the procedure you would use with the **!pte** extension to determine the corresponding physical address:

**Converting a virtual address to a physical address using !pte**

1.  Make sure that you are working in hexadecimal. If necessary, set the current base with the [**N 16**](n--set-number-base-.md) command.

2.  Determine the *byte index* of the address. This number is equal to the lowest 12 bits of the virtual address. Thus, the virtual address 0x0012F980 has a byte index of 0x980.

3.  Set the [process context](changing-contexts.md#process-context) to the desired process:

    ```dbgcmd
    kd> !process 0 0
    **** NT ACTIVE PROCESS DUMP ****
    ....
    PROCESS ff779190  SessionId: 0  Cid: 04fc    Peb: 7ffdf000  ParentCid: 0394
        DirBase: 098fd000  ObjectTable: e1646b30  TableSize:   8.
        Image: MyApp.exe

    kd> .process /p ff779190
    Implicit process is now ff779190
    .cache forcedecodeuser done
    ```

4.  Use the [**!pte**](-pte.md) extension with the virtual address as its argument. This displays information in two columns. The left column describes the page directory entry (PDE) for this address; the right column describes its page table entry (PTE):

    ```dbgcmd
    kd> !pte 12f980
                   VA 0012f980
    PDE at   C0300000        PTE at C00004BC
    contains 0BA58067      contains 09DE9067
    pfn ba58 ---DA--UWV    pfn 9de9 ---DA--UWV
    ```

5.  Look in the last row of the right column. The notation "pfn 9de9" appears. The number 0x9DE9 is the *page frame number* (PFN) of this PTE. Multiply the page frame number by 0x1000 (for example, shift it left 12 bits). The result, 0x09DE9000, is the physical address of the beginning of the page.

6.  Add the byte index to the address of the beginning of the page: 0x09DE9000 + 0x980 = 0x09DE9980. This is the desired physical address.

This is the same result obtained by the earlier method.

### <span id="converting_addresses_by_hand"></span><span id="CONVERTING_ADDRESSES_BY_HAND"></span>Converting Addresses By Hand

Although the **!ptov** and **pte** extensions supply the fastest way to convert virtual addresses to physical addresses, this conversion can be done manually as well. A description of this process will shed light on some of the details of the virtual memory architecture.

Memory structures vary in size, depending on the processor and the hardware configuration. This example is taken from an x86 system that does not have Physical Address Extension (PAE) enabled.

Using 0x0012F980 again as the virtual address, you first need to convert it to binary, either by hand or by using the [**.formats (Show Number Formats)**](-formats--show-number-formats-.md) command:

```dbgcmd
kd> .formats 12f980
Evaluate expression:
  Hex:     0012f980
  Decimal: 1243520
  Octal:   00004574600
  Binary:  00000000 00010010 11111001 10000000
  Chars:   ....
  Time:    Thu Jan 15 01:25:20 1970
  Float:   low 1.74254e-039 high 0
  Double:  6.14381e-318
```

This virtual address is a combination of three fields. Bits 0 to 11 are the byte index. Bits 12 to 21 are the page table index. Bits 22 to 31 are the page directory index. Separating the fields, you have:

```dbgcmd
0x0012F980  =  0y  00000000 00   010010 1111   1001 10000000
```

This exposes the three parts of the virtual address:

-   Page directory index = 0y0000000000 = 0x0

-   Page table index = 0y0100101111 = 0x12F

-   Byte index = 0y100110000000 = 0x980

You then need three additional pieces of information for your system.

-   The size of each PTE. This is 4 bytes on non-PAE x86 systems.

-   The size of a page. This is 0x1000 bytes.

-   The PTE\_BASE virtual address. On a non-PAE system, this is 0xC0000000.

Using this data, you can compute the address of the PTE itself:

```dbgcmd
PTE address   =   PTE_BASE  
                + (page directory index) * PAGE_SIZE
                + (page table index) * sizeof(MMPTE)
              =   0xc0000000
                + 0x0   * 0x1000
                + 0x12F * 4
              =   0xC00004BC
```

This is the address of the PTE. The PTE is a 32-bit DWORD. Examine its contents:

```dbgcmd
kd> dd 0xc00004bc L1
c00004bc  09de9067
```

This PTE has value 0x09DE9067. It is made of two fields:

-   The low 12 bits of the PTE are the *status flags*. In this case, these flags equal 0x067 -- or in binary, 0y000001100111. For an explanation of the status flags, see the [**!pte**](-pte.md) reference page.

-   The high 20 bits of the PTE are equal to the *page frame number* (PFN) of the PTE. In this case, the PFN is 0x09DE9.

The first physical address on the physical page is the PFN multiplied by 0x1000 (shifted left 12 bits). The byte index is the offset on this page. Thus,the physical address you are looking for is 0x09DE9000 + 0x980 = 0x09DE9980. This is the same result obtained by the earlier methods.

 

 





