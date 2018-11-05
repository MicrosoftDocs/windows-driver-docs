---
title: Activation Context
description: Activation Context
ms.assetid: 76584379-2AEF-47e0-B14E-C7698903658F
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Activation Context


TAEF provides a mechanism to specify the 'Activation Context' under which the test should be run.

Providing the 'Activation context' enables users to choose a particular version binary from various side-by-side assemblies in the system. The required 'Activation context' is specified in a manifest file and can be passed to TAEF through the 'ActivationContext' property. The 'ActivationContext' property can be specified as a runtime parameter or as test metadata.

## <span id="Sample_Activation_Context_manifest_file"></span><span id="sample_activation_context_manifest_file"></span><span id="SAMPLE_ACTIVATION_CONTEXT_MANIFEST_FILE"></span>Sample Activation Context manifest file


```cpp
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
  <dependency>
    <dependentAssembly>
      <assemblyIdentity type="win32" name="Microsoft.Windows.Common-Controls" version="6.0.0.0" 
        processorArchitecture="*" publicKeyToken="6595b64144ccf1df"/>
    </dependentAssembly>
  </dependency>
</assembly>
```

The manifest file, **'Comctlv6.manifest'**, that is shown above specifies that version 6 of the comctl32.dll is to be used during test execution. To learn more about manifest files, see [Manifest files reference](https://msdn.microsoft.com/library/aa375632(VS.85).aspx)

## <span id="Specifying_ActivationContext_manifest_at_the_Command_Prompt"></span><span id="specifying_activationcontext_manifest_at_the_command_prompt"></span><span id="SPECIFYING_ACTIVATIONCONTEXT_MANIFEST_AT_THE_COMMAND_PROMPT"></span>Specifying ActivationContext manifest at the Command Prompt


``` syntax
te MyUnitTest.dll /ActivationContext:ComctlV6.manifest
```

This command executes all the tests in 'MyUnitTest.dll' by using the activation context that is specified in ComctlV6.manifest file

## <span id="Specifying_ActivationContext_manifest_as_Test_metadata"></span><span id="specifying_activationcontext_manifest_as_test_metadata"></span><span id="SPECIFYING_ACTIVATIONCONTEXT_MANIFEST_AS_TEST_METADATA"></span>Specifying ActivationContext manifest as Test metadata


If you intend to run only specific test cases under a given activation context, you can do that by setting the value of the 'ActivationContext' property to your manifest file on the test method. For example the following test method declaration runs only the test method 'MyTestMethod' under the specified activation context while running other tests under the default context:

```cpp
        BEGIN_TEST_METHOD(MyTestMethod)
            TEST_METHOD_PROPERTY(L"ActivationContext", L"ComctlV6.manifest")
        END_TEST_METHOD()
```

Note that the 'ActivationContext' property can be set at class and assembly levels like other metadata properties.









