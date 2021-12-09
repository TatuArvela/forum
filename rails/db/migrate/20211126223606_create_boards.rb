class CreateBoards < ActiveRecord::Migration[6.1]
  def change
    create_table :boards do |t|
      t.string :title
      t.text :description
      t.references :created_by, foreign_key: { to_table: :users }, null: false
      t.references :updated_by, foreign_key: { to_table: :users }, null: false

      t.timestamps
    end
  end
end
