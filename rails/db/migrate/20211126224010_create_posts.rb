class CreatePosts < ActiveRecord::Migration[6.1]
  def change
    create_table :posts do |t|
      t.text :message
      t.references :thread, foreign_key: { to_table: :forum_threads }, null: false
      t.references :created_by, foreign_key: { to_table: :users }, null: false
      t.references :updated_by, foreign_key: { to_table: :users }, null: false

      t.timestamps
    end
  end
end
