class CreateForumThreads < ActiveRecord::Migration[6.1]
  def change
    create_table :forum_threads do |t|
      t.string :title
      t.references :board, foreign_key: { to_table: :boards }, null: false
      t.references :created_by, foreign_key: { to_table: :users }, null: false
      t.references :updated_by, foreign_key: { to_table: :users }, null: false

      t.timestamps
    end
  end
end
