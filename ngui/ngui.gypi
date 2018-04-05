{
  'variables': {
    'gui_glsl_files': [
      'gl/glsl/_version.glsl',
      'gl/glsl/_util.glsl',
      'gl/glsl/_box.glsl',
      'gl/glsl/_box-radius.glsl',
      'gl/glsl/sprite.glsl',
      'gl/glsl/box-image.glsl',
      'gl/glsl/box-yuv420p-image.glsl',
      'gl/glsl/box-yuv420sp-image.glsl',
      'gl/glsl/box-border.glsl',
      'gl/glsl/box-color.glsl',
      'gl/glsl/box-shadow.glsl',
      'gl/glsl/box-image-radius.glsl',
      'gl/glsl/box-border-radius.glsl',
      'gl/glsl/box-color-radius.glsl',
      'gl/glsl/text-box-color.glsl',
      'gl/glsl/text-texture.glsl',
      'gl/glsl/text-vertex.glsl',
      'gl/glsl/gen-texture.glsl',
    ],
    'gui_glsl_cpp_files': [
      '../out/glsl-sprite.h',
      '../out/glsl-sprite.cc',
      '../out/glsl-box-image.h',
      '../out/glsl-box-image.cc',
      '../out/glsl-box-yuv420p-image.h',
      '../out/glsl-box-yuv420p-image.cc',
      '../out/glsl-box-yuv420sp-image.h',
      '../out/glsl-box-yuv420sp-image.cc',
      '../out/glsl-box-border.h',
      '../out/glsl-box-border.cc',
      '../out/glsl-box-color.h',
      '../out/glsl-box-color.cc',
      '../out/glsl-box-shadow.h',
      '../out/glsl-box-shadow.cc',
      '../out/glsl-box-image-radius.h',
      '../out/glsl-box-image-radius.cc',
      '../out/glsl-box-border-radius.h',
      '../out/glsl-box-border-radius.cc',
      '../out/glsl-box-color-radius.h',
      '../out/glsl-box-color-radius.cc',
      '../out/glsl-text-box-color.h',
      '../out/glsl-text-box-color.cc',
      '../out/glsl-text-texture.h',
      '../out/glsl-text-texture.cc',
      '../out/glsl-text-vertex.h',
      '../out/glsl-text-vertex.cc',
      '../out/glsl-gen-texture.h',
      '../out/glsl-gen-texture.cc',
    ],
    'gui_default_font_files': [
      'font/DejaVuSerif.ttf',
      'font/icomoon.ttf',
    ],
  },
  'targets':[{
    'target_name': 'ngui-gui',
    'type': '<(library)',
    'include_dirs': [
      '..',
      '../out',
    ],
    'dependencies': [
      'ngui-base', 
      'depe/tess2/tess2.gyp:tess2', 
      'depe/freetype2/freetype2.gyp:ft2',
      'depe/ffmpeg/ffmpeg.gyp:ffmpeg',
      'depe/tinyxml2/tinyxml2.gyp:tinyxml2',
    ],
    'direct_dependent_settings': {
      'include_dirs': [ '..' ],
    },
    'sources': [
      '<@(gui_glsl_cpp_files)',
      '../out/font-native.cc',
      'player.h',
      'audio-player.h',
      'div.h',
      'indep.h',
      'box-shadow-1.h',
      'image.h',
      'bezier.h',
      'display-port.h',
      'event.h',
      'image-codec.h',
      'label.h',
      'layout.h',
      'box.h',
      'text-font.h',
      'pre-render.h',
      'mathe.h',
      'media-codec.h',
      'view.h',
      'draw.h',
      'root.h',
      'sprite.h',
      'scroll.h',
      'span.h',
      'hybrid.h',
      'text-node.h',
      'texture.h',
      'video.h',
      'value.h',
      'pcm-player.h',
      'action.h',
      'action.cc.inl',
      'action.cc',
      'app.h',
      'app.cc',
      'app-1.h',
      'audio-player.cc',
      'div.cc',
      'indep.cc',
      'gradient-1.h',
      'gradient.cc',
      'box-shadow.cc',
      'limit.h',
      'limit.cc',
      'limit-indep.h',
      'limit-indep.cc',
      'image.cc',
      'bezier.cc',
      'event.cc',
      'display-port.cc',
      'font.h',
      'font/font-1.h',
      'font/font.cc',
      'font/font.cc.1.inl',
      'font/font.cc.3.inl',
      'font/font.cc.font.inl',
      'font/font.cc.family.inl',
      'font/font.cc.glyph.inl',
      'image/codec.cc',
      'image/codec-tga.cc',
      'image/codec-pvrtc.cc',
      'pre-render.cc',
      'mathe.cc',
      'media-codec.cc',
      'media-codec-1.h',
      'media-codec-1.cc',
      'media-codec-software.cc',
      'label.cc',
      'layout.cc',
      'box.cc',
      'text-rows.cc',
      'text-rows.h',
      'view.cc',
      'draw.cc',
      'gl/gl.cc',
      'gl/gl.h',
      'gl/gl-draw.cc',
      'gl/gl-texture.cc',
      'gl/gl-font.cc',
      'root.cc',
      'sprite.cc',
      'scroll.cc',
      'span.cc',
      'hybrid.cc',
      'text-font.cc',
      'text-node.cc',
      'texture.cc',
      'video.cc',
      'value.cc',
      'panel.h',
      'panel.cc',
      'button.h',
      'button.cc',
      'keyboard.h',
      'keyboard.cc',
      'css.h',
      'css.cc.inl',
      'css.cc',
      'property.h',
      'property.cc',
      'text.h',
      'text.cc',
      'clip.h',
      'clip.cc',
      'input.h',
      'input.cc',
      'textarea.h',
      'textarea.cc',
    ],
    'conditions': [
      ['os=="android"', {
        'sources': [
          'os/android-gl-1.h',
          'os/android-gl.cc',
          'os/android-app.cc',
          'os/android-media-codec.cc',
          'os/android-pcm-player.cc',
          'os/android-pcm-audio-track.cc',
          'os/android-keyboard.cc',
          'os/android/com/ngui/MainActivity.java',
        ],
        'link_settings': { 
          'libraries': [ '-lGLESv3', '-lEGL', '-lOpenSLES', '-lmediandk' ],
        },
      }],
      ['os not in "ios osx"', { 
        'dependencies': [
          'depe/libgif/libgif.gyp:libgif', 
          'depe/libjpeg-turbo/libjpeg.gyp:libjpeg', 
          'depe/libpng/libpng.gyp:libpng',
          'depe/libwebp/libwebp.gyp:libwebp',
        ],
        'sources': [
          'image/codec-gif.cc',
          'image/codec-jpeg.cc',
          'image/codec-png.cc',
          'image/codec-webp.cc',
        ]
      }],
      ['os=="ios"', {
        'sources':[
          'os/ios-app.h',
          'os/ios-app.mm',
          'os/ios-ime-receiver-1.h',
          'os/ios-ime-receiver.mm',
          'os/ios-gl-1.h',
          'os/ios-gl.mm',
          'os/ios-image-codec.mm',
          'os/mac-media-codec.mm',
          'os/mac-pcm-player.mm',
          'os/mac-keyboard.mm',
        ],
        'link_settings': {
          'libraries': [
            '$(SDKROOT)/System/Library/Frameworks/OpenGLES.framework',
            '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
            '$(SDKROOT)/System/Library/Frameworks/UIKit.framework',
            '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
            '$(SDKROOT)/System/Library/Frameworks/MessageUI.framework',
          ]
        },
      }],
      ['os=="osx"', {
        'sources': [
          'os/osx-app-1.h',
          'os/osx-app.mm',
          'os/osx-image-codec.mm',
          'os/mac-media-codec.mm',
          'os/mac-pcm-player.mm',
          'os/mac-keyboard.mm',
        ],
        'link_settings': {
          'libraries': [
            '$(SDKROOT)/System/Library/Frameworks/OpenGL.framework',
            '$(SDKROOT)/System/Library/Frameworks/CoreGraphics.framework',
            '$(SDKROOT)/System/Library/Frameworks/AppKit.framework',
            '$(SDKROOT)/System/Library/Frameworks/QuartzCore.framework',
          ]
        },
      }],
      # conditions end
    ],
    'actions': [
      {
        'action_name': 'gen_glsl_natives',
        'inputs': [
          '../tools/gen-glsl-natives.js',
          '<@(gui_glsl_files)',
        ],
        'outputs': [
          '<@(gui_glsl_cpp_files)',
        ],
        'action': [
          '<(node)',
          '<@(_inputs)',
          'glsl-',
          '',
        ],
      },
      {
        'action_name': 'gen_font_natives',
        'inputs': [
          '../tools/gen-font-natives.js',
          '<@(gui_default_font_files)',
        ],
        'outputs': [
          '../out/font-native.h',
          '../out/font-native.cc',
        ],
        'action': [
          '<(node)',
          '<@(_inputs)',
          '<@(_outputs)',
        ],
      },
    ],
    # end
  }]
}
