class CreateItems < ActiveRecord::Migration[5.0]
  def change
    create_table :items do |t|
      t.string :input
      t.string :output

      t.timestamps
    end
  end
end
