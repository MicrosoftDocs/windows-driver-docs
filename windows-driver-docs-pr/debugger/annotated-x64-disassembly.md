---
title: Annotated x64 Disassembly
description: Annotated x64 Disassembly
ms.assetid: 67930062-8a3a-460f-ae56-248d2a8e131e
keywords: ["x64 processor, annotated disassembly"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Annotated x64 Disassembly


## <span id="ddk_annotated_x64_disassembly_dbg"></span><span id="DDK_ANNOTATED_X64_DISASSEMBLY_DBG"></span>


The following very simple function illustrates the x64 calling convention.

```cpp
int Simple(int i, int j)
{
    return i*5 + j + 3;
}
```

This compiles to code like this:

```dbgcmd
01001080 lea     eax,[rdx+rcx*4]        ; eax = rdx+rcx*4
01001083 lea     eax,[rcx+rax+0x3]      ; eax = rcx+rax+3
01001087 ret
```

The *i* and *j* parameters are passed in the **ecx** and **edx** registers, respectively. Since there are only two parameters, the routine does not use the stack at all.

The particular code generated exploits three tricks, one of which is specific to the x64:

1.  The **lea** operation can be used to perform a series of simple arithmetic operations as a single operation. The first instruction stores *j+i*\*4 in **eax**, and the second instruction adds *i*+3 to the result, for a total of *j*+*i*\*5+3.

2.  Many operations, such as addition and multiplication, can be done with extra precision, and then truncated to the correct precision. In this instance, the code uses 64-bit addition and multiplication. We can safely truncate the result to 32 bits.

3.  On the x64, any operation that outputs to a 32-bit register automatically zero-extends the result. In this case, outputting to **eax** has the effect of truncating the result to 32 bits.

Return values are passed in the **rax** register. In this case, the result is already in the **rax** register, so the function returns.

Next we consider a more complicated function to demonstrate typical x64 disassembly:

```cpp
HRESULT Meaningless(IDispatch *pdisp, DISPID dispid, BOOL fUnique, LPCWSTR pszExe)
{
    IQueryAssociations *pqa;
    HRESULT hr = AssocCreate(CLSID_QueryAssociations, IID_IQueryAssociations, (void**)&pqa);
    if (SUCCEEDED(hr)) {
        hr = pqa->Init(ASSOCF_INIT_BYEXENAME, pszExe, NULL, NULL);
        if (SUCCEEDED(hr)) {
            WCHAR wszName[MAX_PATH];
            DWORD cchName = MAX_PATH;
            hr = pqa->GetString(0, ASSOCSTR_FRIENDLYAPPNAME, NULL, wszName, &cchName);
            if (SUCCEEDED(hr)) {
                VARIANTARG rgvarg[2] = { 0 };
                V_VT(&rgvarg[0]) = VT_BSTR;
                V_BSTR(&rgvarg[0]) = SysAllocString(wszName);
                if (V_BSTR(&rgvarg[0])) {
                    DISPPARAMS dp;
                    LONG lUnique = InterlockedIncrement(&lCounter);
                    V_VT(&rgvarg[1]) = VT_I4;
                    V_I4(&rgvarg[1]) = fUnique ? lUnique : 0;
                    dp.rgvarg = rgvarg;
                    dp.cArgs = 2;
                    dp.rgdispidNamedArgs = NULL;
                    dp.cNamedArgs = 0;
                    hr = pdisp->Invoke(dispid, IID_NULL, 0, DISPATCH_METHOD, &dp, NULL, NULL, NULL);
                    VariantClear(&rgvarg[0]);
                    VariantClear(&rgvarg[1]);
                } else {
                    hr = E_OUTOFMEMORY;
                }
            }
        }
        pqa->Release();
    }
    return hr;
}
```

We'll go through this function and the equivalent assembly line by line.

When entered, the function's parameters are stored as follows:

-   **rcx** = *pdisp*.

-   **rdx** = *dispid*.

-   **r8** = *fUnique*.

-   **r9** = *pszExe*.

Recall that the first four parameters are passed in registers. Since this function has only four registers, none are passed on the stack.

The assembly begins as follows:

```dbgcmd
Meaningless:
010010e0 push    rbx                    ; save
010010e1 push    rsi                    ; save
010010e2 push    rdi                    ; save
010010e3 push    r12d                   ; save
010010e5 push    r13d                   ; save
010010e7 push    r14d                   ; save
010010e9 push    r15d                   ; save
010010eb sub     rsp,0x2c0              ; reserve stack
010010f2 mov     rbx,r9                 ; rbx = pszExe
010010f5 mov     r12d,r8d               ; r12 = fUnique (zero-extend)
010010f8 mov     r13d,edx               ; r13 = dispid  (zero-extend)
010010fb mov     rsi,rcx                ; rsi = pdisp
```

The function begins by saving nonvolatile registers, and then reserving stack space for local variables. It then saves parameters in nonvolatile registers. Note that the destination of the middle two **mov** instructions is a 32-bit register, so they are implicitly zero-extended to 64 bits.

```dbgcmd
    IQueryAssociations *pqa;
    HRESULT hr = AssocCreate(CLSID_QueryAssociations, IID_IQueryAssociations, (void**)&pqa);
```

The first parameter to **AssocCreate** is a 128-bit CLSID passed by value. Since this doesn't fit in a 64-bit register, the CLSID is copied to the stack, and a pointer to the stack location is passed instead.

```dbgcmd
010010fe movdqu  xmm0,oword ptr [CLSID_QueryAssociations (01001060)]
01001106 movdqu  oword ptr [rsp+0x60],xmm0  ; temp buffer for first parameter
0100110c lea     r8,[rsp+0x58]          ; arg3 = &pqa
01001111 lea rdx,[IID_IQueryAssociations (01001070)] ; arg2 = &IID_IQueryAssociations
01001118 lea     rcx,[rsp+0x60]         ; arg1 = &temporary
0100111d call qword ptr [_imp_AssocCreate (01001028)] ; call
```

The **movdqu** instruction transfers 128-bits values to and from **xmm***n* registers. In this instance, the assembly code uses it to copy the CLSID to the stack. The pointer to the CLSID is passed in **r8**. The other two arguments are passed in **rcx** and **rdx**.

```dbgcmd
    if (SUCCEEDED(hr)) {

01001123 test    eax,eax
01001125 jl      ReturnEAX (01001281)
```

The code checks to see if the return value is a success.

```dbgcmd
        hr = pqa->Init(ASSOCF_INIT_BYEXENAME, pszExe, NULL, NULL);

0100112b mov     rcx,[rsp+0x58]         ; arg1 = pqa
01001130 mov     rax,[rcx]              ; rax = pqa.vtbl
01001133 xor     r14d,r14d              ; r14 = 0
01001136 mov     [rsp+0x20],r14         ; arg5 = 0
0100113b xor     r9d,r9d                ; arg4 = 0
0100113e mov     r8,rbx                 ; arg3 = pszExe
01001141 mov     r15d,0x2               ; r15 = 2 (for later)
01001147 mov     edx,r15d               ; arg2 = 2 (ASSOCF_INIT_BY_EXENAME)
0100114a call    qword ptr [rax+0x18]   ; call Init method
```

This is an indirect function call using a C++ vtable. The **this** pointer is passed in **rcx** as the first parameter. The first three parameters are passed in registers, while the final parameter is passed on the stack. The function reserves 16 bytes for the parameters passed in registers, so the fifth parameter begins at **rsp**+0x20.

```dbgcmd
        if (SUCCEEDED(hr)) {

0100114d mov     ebx,eax                ; ebx = hr
0100114f test    ebx,ebx                ; FAILED?
01001151 jl      ReleasePQA (01001274)  ; jump if so
```

The assembly-language code saves the result in **ebx**, and checks to see if it's a success code.

```dbgcmd
            WCHAR wszName[MAX_PATH];
            DWORD cchName = MAX_PATH;
            hr = pqa->GetString(0, ASSOCSTR_FRIENDLYAPPNAME, NULL, wszName, &cchName);
            if (SUCCEEDED(hr)) {

01001157 mov     dword ptr [rsp+0x50],0x104 ; cchName = MAX_PATH
0100115f mov     rcx,[rsp+0x58]         ; arg1 = pqa
01001164 mov     rax,[rcx]              ; rax = pqa.vtbl
01001167 lea     rdx,[rsp+0x50]         ; rdx = &cchName
0100116c mov     [rsp+0x28],rdx         ; arg6 = cchName
01001171 lea     rdx,[rsp+0xb0]         ; rdx = &wszName[0]
01001179 mov     [rsp+0x20],rdx         ; arg5 = &wszName[0]
0100117e xor     r9d,r9d                ; arg4 = 0
01001181 mov     r8d,0x4                ; arg3 = 4 (ASSOCSTR_FRIENDLYNAME)
01001187 xor     edx,edx                ; arg2 = 0
01001189 call    qword ptr [rax+0x20]   ; call GetString method
0100118c mov     ebx,eax                ; ebx = hr
0100118e test    ebx,ebx                ; FAILED?
01001190 jl      ReleasePQA (01001274)  ; jump if so
```

Once again, we set up the parameters and call a function, then test the return value for success.

```dbgcmd
                VARIANTARG rgvarg[2] = { 0 };

01001196 lea     rdi,[rsp+0x82]         ; rdi = &rgvarg
0100119e xor     eax,eax                ; rax = 0
010011a0 mov     ecx,0x2e               ; rcx = sizeof(rgvarg)
010011a5 rep     stosb                  ; Zero it out
```

The idiomatic method for zeroing out a buffer on x64 is the same as x86.

```dbgcmd
                V_VT(&rgvarg[0]) = VT_BSTR;
                V_BSTR(&rgvarg[0]) = SysAllocString(wszName);
                if (V_BSTR(&rgvarg[0])) {

010011a7 mov     word ptr [rsp+0x80],0x8 ; V_VT(&rgvarg[0]) = VT_BSTR
010011b1 lea     rcx,[rsp+0xb0]         ; arg1 = &wszName[0]
010011b9 call    qword ptr [_imp_SysAllocString (01001010)] ; call
010011bf mov     [rsp+0x88],rax         ; V_BSTR(&rgvarg[0]) = result
010011c7 test    rax,rax                ; anything allocated?
010011ca je      OutOfMemory (0100126f) ; jump if failed

                    DISPPARAMS dp;
                    LONG lUnique = InterlockedIncrement(&lCounter);

010011d0 lea     rax,[lCounter (01002000)]
010011d7 mov     ecx,0x1
010011dc lock    xadd [rax],ecx             ; interlocked exchange and add
010011e0 add     ecx,0x1
```

**InterlockedIncrement** compiles directly to machine code. The **lock xadd** instruction performs an atomic exchange and add. The final result is stored in **ecx**.

```dbgcmd
                    V_VT(&rgvarg[1]) = VT_I4;
                    V_I4(&rgvarg[1]) = fUnique ? lUnique : 0;

010011e3 mov     word ptr [rsp+0x98],0x3    ; V_VT(&rgvarg[1]) = VT_I4;
010011ed mov     eax,r14d                   ; rax = 0 (r14d is still zero)
010011f0 test    r12d,r12d                  ; fUnique set?
010011f3 cmovne  eax,ecx                    ; if so, then set rax=lCounter
010011f6 mov     [rsp+0xa0],eax             ; V_I4(&rgvarg[1]) = ...
```

Since x64 supports the **cmov** instruction, the **?:** construct can be compiled without using a jump.

```dbgcmd
                    dp.rgvarg = rgvarg;
                    dp.cArgs = 2;
                    dp.rgdispidNamedArgs = NULL;
                    dp.cNamedArgs = 0;

010011fd lea     rax,[rsp+0x80]             ; rax = &rgvarg[0]
01001205 mov     [rsp+0x60],rax             ; dp.rgvarg = rgvarg
0100120a mov     [rsp+0x70],r15d            ; dp.cArgs = 2 (r15 is still 2)
0100120f mov     [rsp+0x68],r14             ; dp.rgdispidNamedArgs = NULL
01001214 mov     [rsp+0x74],r14d            ; dp.cNamedArgs = 0
```

This code initializes the rest of the members of DISPPARAMS. Note that the compiler reuses the space on the stack previously used by the CLSID.

```dbgcmd
                    hr = pdisp->Invoke(dispid, IID_NULL, 0, DISPATCH_METHOD, &dp, NULL, NULL, NULL);

01001219 mov     rax,[rsi]                  ; rax = pdisp.vtbl
0100121c mov     [rsp+0x40],r14             ; arg9 = 0
01001221 mov     [rsp+0x38],r14             ; arg8 = 0
01001226 mov     [rsp+0x30],r14             ; arg7 = 0
0100122b lea     rcx,[rsp+0x60]             ; rcx = &dp
01001230 mov     [rsp+0x28],rcx             ; arg6 = &dp
01001235 mov     word ptr [rsp+0x20],0x1    ; arg5 = 1 (DISPATCH_METHOD)
0100123c xor     r9d,r9d                    ; arg4 = 0
0100123f lea     r8,[GUID_NULL (01001080)]  ; arg3 = &IID_NULL
01001246 mov     edx,r13d                   ; arg2 = dispid
01001249 mov     rcx,rsi                    ; arg1 = pdisp
0100124c call    qword ptr [rax+0x30]       ; call Invoke method
0100124f mov     ebx,eax                    ; hr = result
```

The code then sets up the parameters and calls the **Invoke** method.

```dbgcmd
                    VariantClear(&rgvarg[0]);
                    VariantClear(&rgvarg[1]);

01001251 lea     rcx,[rsp+0x80]             ; arg1 = &rgvarg[0]
01001259 call    qword ptr [_imp_VariantClear (01001018)]
0100125f lea     rcx,[rsp+0x98]             ; arg1 = &rgvarg[1]
01001267 call    qword ptr [_imp_VariantClear (01001018)]
0100126d jmp     ReleasePQA (01001274)
```

The code finishes up the current branch of the conditional, and skips over the **else** branch.

```dbgcmd
                } else {
                    hr = E_OUTOFMEMORY;
                }
            }

OutOfMemory:
0100126f mov     ebx,0x8007000e             ; hr = E_OUTOFMEMORY
        pqa->Release();
ReleasePQA:
01001274 mov     rcx,[rsp+0x58]             ; arg1 = pqa
01001279 mov     rax,[rcx]                  ; rax = pqa.vtbl
0100127c call    qword ptr [rax+0x10]       ; release
```

The **else** branch.

```dbgcmd
    return hr;
}

0100127f mov     eax,ebx                    ; rax = hr (for return value)
ReturnEAX:
01001281 add     rsp,0x2c0                  ; clean up the stack
01001288 pop     r15d                       ; restore
0100128a pop     r14d                       ; restore
0100128c pop     r13d                       ; restore
0100128e pop     r12d                       ; restore
01001290 pop     rdi                        ; restore
01001291 pop     rsi                        ; restore
01001292 pop     rbx                        ; restore
01001293 ret                                ; return (do not pop arguments)
```

The return value is stored in **rax**, and then the non-volatile registers are restored before returning.

 

 





