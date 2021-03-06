{
  'defines': [
    'UCHARDET_VERSION="0.0.6"'
  ],
  'variables': {
    'url': 'https://www.freedesktop.org/wiki/Software/uchardet/',
    'bugreport': 'https://bugs.freedesktop.org/enter_bug.cgi?product=uchardet',
    'version_major': '0',
    'version_minor': '0',
    'version_revision': '0',
    'version': '$(UCHARDET_VERSION)',
    'product_name': 'libuchardet',
  },
  'target_defaults': {
    'cflags': [
      '-std=c++11',
      '-Wall',
    ],
    'cflags!': [
      '-fno-exceptions'
    ],
    'cflags_cc!': [
      '-fno-exceptions'
    ],
    # OSX
    'xcode_settings': {
      'CLANG_CXX_LANGUAGE_STANDARD': 'c++11',
      'CLANG_CXX_LIBRARY': 'libc++',
      'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
      'GCC_ENABLE_CPP_RTTI': 'YES',
      'MACOSX_DEPLOYMENT_TARGET': '10.12',
    },
    # Windows
    'msvs_settings': {
      'VCLinkerTool': {
        'AdditionalLibraryDirectories': [
          # LDFlags
        ]
      }
    },
    'configurations': {
      # [Configuration] Debug
      'Debug': {
        'defines': [
          'DEBUG',
          '_DEBUG'
        ],
        # Windows
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 1,
          },
          'VCLinkerTool': {
            'LinkTimeCodeGeneration': 1,
            'OptimizeReferences': 2,
            'EnableCOMDATFolding': 2,
            'LinkIncremental': 1,
            'GenerateDebugInformation': 'true',
          }
        },
        'xcode_settings': {
          'GENERATE_DEBUG_SYMBOLS': 'YES',
        }
      },
      # [Configuration] Release
      'Release': {
        # Windows
        'msvs_settings': {
          'VCCLCompilerTool': {
            'RuntimeLibrary': 0,
            'Optimization': 3,
            'FavorSizeOrSpeed': 1,
            'InlineFunctionExpansion': 2,
            'WholeProgramOptimization': 'true',
            'OmitFramePointers': 'true',
            'EnableFunctionLevelLinking': 'true',
            'EnableIntrinsicFunctions': 'true'
          },
          'VCLinkerTool': {
            'LinkTimeCodeGeneration': 1,
            'OptimizeReferences': 2,
            'EnableCOMDATFolding': 2,
            'LinkIncremental': 1,
          }
        },
      }
    },
    'conditions': [
      # OSX
      ['OS=="mac"', {
        'cflags+': [
          '-stdlib=libc++',
        ],
      }],
      # Linux
      ['OS=="linux"', {
        'cflags+': [
          '-fPIC',
          '-mfpmath=sse',
          '-msse2',
          '-O3',
          '-std=gnu++11',
          '-Wall',
        ],
      }],
      # Windows
      ['OS=="win"', {
        'cflags_cc+': [
          '-std=c++0x',
        ]
      }]
    ],
  }
}
