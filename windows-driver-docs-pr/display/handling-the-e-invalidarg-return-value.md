---
title: Handling the E_INVALIDARG Return Value
description: Learn the rules and best practices for handling E_INVALIDARG in user-mode display drivers, including when to propagate errors from runtime functions.
keywords:
- user-mode display drivers WDK Windows Vista , E_INVALIDARG return value
- E_INVALIDARG return value WDK display
ms.date: 11/11/2025
ms.topic: concept-article
ai.usage: ai-assisted
---

# Handling the E_INVALIDARG return value

User-mode display drivers (UMDs) must follow specific rules when handling the `E_INVALIDARG` error code. This article explains when and how to properly handle this error value in your driver code.

## Overview

The `E_INVALIDARG` error code indicates that one or more arguments passed to a function are invalid. In the context of UMDs, there's an important distinction:

- **Driver-generated errors**: Your driver shouldn't fail any of its functions by returning `E_INVALIDARG` to the Direct3D runtime.
- **Runtime-propagated errors**: If your driver receives `E_INVALIDARG` from a runtime-supplied function, it must propagate that error back to the runtime.

This rule creates a clear error attribution boundary between driver code and runtime code.

## Why this rule exists

The `E_INVALIDARG` propagation rule serves several important purposes:

- **Clear responsibility boundaries**: When the Direct3D runtime receives `E_INVALIDARG`, it knows the error originated from runtime-supplied functions, not from the driver itself.

- **Debugging efficiency**: Developers can quickly identify whether an `E_INVALIDARG` error indicates that:
   - The driver is calling runtime functions with invalid parameters.
   - Malicious code is interfering with the graphics stack.
   - Runtime internal issues that need investigation.

- **Security and reliability**: By requiring drivers to propagate (not generate) `E_INVALIDARG`, the system can detect anomalous behavior that might indicate security threats or stack corruption.

## Implementation guidelines

### Basic error handling pattern

When your driver calls a runtime-supplied function, always check the return value and propagate `E_INVALIDARG` if received:

```cpp
HRESULT MyDriverFunction(/* parameters */)
{
    HRESULT hr;
    
    // Call a runtime-supplied function
    hr = pRuntimeCallbacks->pfnSomeRuntimeFunction(/* arguments */);
    
    // Propagate E_INVALIDARG if received from runtime
    if (hr == E_INVALIDARG)
    {
        // The runtime detected invalid arguments we passed
        // Must return this error back to the runtime
        return E_INVALIDARG;
    }
    
    // Handle other error codes appropriately
    if (FAILED(hr))
    {
        // Use appropriate error code for driver-specific failures
        return hr; // or return E_FAIL, E_OUTOFMEMORY, etc.
    }
    
    // Continue with driver logic
    // ...
    
    return S_OK;
}
```

### Don't generate E_INVALIDARG in your driver

Never generate `E_INVALIDARG` directly in your driver code:

```cpp
// INCORRECT - Do not do this
HRESULT MyDriverFunction(D3DDDIARG_SOMEARGS* pArgs)
{
    if (pArgs == NULL || pArgs->SomeValue > MAX_VALUE)
    {
        // Wrong: Driver should not return E_INVALIDARG for its own validation
        return E_INVALIDARG;  // DO NOT DO THIS
    }
    // ...
}

// CORRECT - Use appropriate error codes for driver-specific validation
HRESULT MyDriverFunction(D3DDDIARG_SOMEARGS* pArgs)
{
    if (pArgs == NULL)
    {
        // Correct: Use E_FAIL or E_POINTER for driver-specific validation
        return E_FAIL;
    }
    
    if (pArgs->SomeValue > MAX_VALUE)
    {
        // Correct: Use E_FAIL or other appropriate error code
        return E_FAIL;
    }
    // ...
}
```

## Example: Calling runtime allocation functions

```cpp
HRESULT MyDriver_CreateResource(HANDLE hDevice, D3DDDIARG_CREATERESOURCE* pResource)
{
    HRESULT hr;
    D3DDDICB_ALLOCATE AllocateData = {0};
    
    // Set up allocation parameters
    AllocateData.pPrivateDriverData = pMyDriverData;
    AllocateData.PrivateDriverDataSize = sizeof(MY_DRIVER_DATA);
    // ... other initialization ...
    
    // Call runtime-supplied allocation function
    hr = pCallbacks->pfnAllocateCb(hDevice, &AllocateData);
    
    if (hr == E_INVALIDARG)
    {
        // Runtime detected invalid allocation parameters
        // This likely indicates a bug in how we set up AllocateData
        // Must propagate this error back to the runtime
        return E_INVALIDARG;
    }
    
    if (FAILED(hr))
    {
        // Handle other allocation failures
        return hr;
    }
    
    // Continue with resource creation
    // ...
    return S_OK;
}
```

## Best practices

- **Use appropriate error codes**: For driver-specific validation failures, use `E_FAIL`, `E_OUTOFMEMORY`, `E_NOTIMPL`, or other appropriate HRESULT values.

- **Always check runtime function return values**: Don't assume runtime functions always succeed.

- **Propagate E_INVALIDARG immediately**: When you receive `E_INVALIDARG` from a runtime function, return it directly without modification.

- **Document unexpected E_INVALIDARG**: If runtime functions return `E_INVALIDARG`, it might indicate a bug in your driver's parameter setup - investigate and fix.

- **Test with Driver Verifier**: Use Driver Verifier during development to catch violations of this error handling rule early.
