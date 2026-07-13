# SketchUp Ruby script — batch-export all saved Scenes as PNG images.
#
# Usage (SketchUp Pro):
#   1. Open your model
#   2. Window > Ruby Console
#   3. load "/path/to/export_scenes.rb"
#   4. ExportScenes.run("C:/path/to/output/folder")
#
# Or from terminal (macOS example):
#   /Applications/SketchUp\ 2024/SketchUp.app/Contents/MacOS/SketchUp my_model.skp \
#     -RubyStartup export_scenes.rb

module ExportScenes
  def self.run(output_dir = nil)
    model = Sketchup.active_model
    pages = model.pages
    if pages.count == 0
      UI.messagebox("No saved Scenes found in this model.")
      return
    end

    out = output_dir || UI.savepanel("Choose export folder", "", "")
    return unless out && !out.empty?

    width  = 4000
    height = 3000

    pages.each do |page|
      pages.selected_page = page
      model.active_view.refresh

      safe_name = page.name.gsub(/[^a-zA-Z0-9_\- ]/, "_").strip.gsub(/\s+/, "_")
      path = File.join(out, "#{safe_name}.png")

      opts = {
        filename: path,
        width: width,
        height: height,
        antialias: true,
        compression: 0.9,
        transparent: false
      }

      model.active_view.write_image(opts)
      puts "Exported scene '#{page.name}' -> #{path}"
    end

    UI.messagebox("Exported #{pages.count} scene(s) to:\n#{out}")
  end
end

ExportScenes.run if defined?(Sketchup)
