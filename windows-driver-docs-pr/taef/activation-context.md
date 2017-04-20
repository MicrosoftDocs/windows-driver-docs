---
title: Activation Context
description: Activation Context
ms.assetid: 76584379-2AEF-47e0-B14E-C7698903658F
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Activation Context


TAEF provides a mechanism to specify the 'Activation Context' under which the test should be run.

Providing the 'Activation context' enables users to choose a particular version binary from various side-by-side assemblies in the system. The required 'Activation context' is specified in a manifest file and can be passed to TAEF through the 'ActivationContext' property. The 'ActivationContext' property can be specified as a runtime parameter or as test metadata.

## <span id="Sample_Activation_Context_manifest_file"></span><span id="sample_activation_context_manifest_file"></span><span id="SAMPLE_ACTIVATION_CONTEXT_MANIFEST_FILE"></span>Sample Activation Context manifest file


```
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

The manifest file, **'Comctlv6.manifest'**, that is shown above specifies that version 6 of the comctl32.dll is to be used during test execution. To learn more about manifest files, refer to [MSDN](http://msdn.microsoft.com/library/aa375632(VS.85).aspx)

## <span id="Specifying_ActivationContext_manifest_at_the_Command_Prompt"></span><span id="specifying_activationcontext_manifest_at_the_command_prompt"></span><span id="SPECIFYING_ACTIVATIONCONTEXT_MANIFEST_AT_THE_COMMAND_PROMPT"></span>Specifying ActivationContext manifest at the Command Prompt


``` syntax
te MyUnitTest.dll /ActivationContext:ComctlV6.manifest
```

This command executes all the tests in 'MyUnitTest.dll' by using the activation context that is specified in ComctlV6.manifest file

## <span id="Specifying_ActivationContext_manifest_as_Test_metadata"></span><span id="specifying_activationcontext_manifest_as_test_metadata"></span><span id="SPECIFYING_ACTIVATIONCONTEXT_MANIFEST_AS_TEST_METADATA"></span>Specifying ActivationContext manifest as Test metadata


If you intend to run only specific test cases under a given activation context, you can do that by setting the value of the 'ActivationContext' property to your manifest file on the test method. For example the following test method declaration runs only the test method 'MyTestMethod' under the specified activation context while running other tests under the default context:

```
        BEGIN_TEST_METHOD(MyTestMethod)
            TEST_METHOD_PROPERTY(L"ActivationContext", L"ComctlV6.manifest")
        END_TEST_METHOD()
```

Note that the 'ActivationContext' property can be set at class and assembly levels like other metadata properties.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[taef\taef]:%20Activation%20Context%20%20RELEASE:%20%289/12/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




