# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# This file is the source Rails uses to define your schema when running `bin/rails
# db:schema:load`. When creating a new database, `bin/rails db:schema:load` tends to
# be faster and is potentially less error prone than running all of your
# migrations from scratch. Old migrations may fail to apply correctly if those
# migrations use external dependencies or application code.
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 2021_11_26_224010) do

  create_table "boards", force: :cascade do |t|
    t.string "title"
    t.text "description"
    t.integer "created_by_id", null: false
    t.integer "updated_by_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["created_by_id"], name: "index_boards_on_created_by_id"
    t.index ["updated_by_id"], name: "index_boards_on_updated_by_id"
  end

  create_table "forum_threads", force: :cascade do |t|
    t.string "title"
    t.integer "board_id", null: false
    t.integer "created_by_id", null: false
    t.integer "updated_by_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["board_id"], name: "index_forum_threads_on_board_id"
    t.index ["created_by_id"], name: "index_forum_threads_on_created_by_id"
    t.index ["updated_by_id"], name: "index_forum_threads_on_updated_by_id"
  end

  create_table "posts", force: :cascade do |t|
    t.text "message"
    t.integer "thread_id", null: false
    t.integer "created_by_id", null: false
    t.integer "updated_by_id", null: false
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.index ["created_by_id"], name: "index_posts_on_created_by_id"
    t.index ["thread_id"], name: "index_posts_on_thread_id"
    t.index ["updated_by_id"], name: "index_posts_on_updated_by_id"
  end

  create_table "users", force: :cascade do |t|
    t.string "username"
    t.boolean "admin"
    t.datetime "created_at", precision: 6, null: false
    t.datetime "updated_at", precision: 6, null: false
    t.string "email", default: "", null: false
    t.string "encrypted_password", default: "", null: false
    t.datetime "remember_created_at"
  end

  add_foreign_key "boards", "users", column: "created_by_id"
  add_foreign_key "boards", "users", column: "updated_by_id"
  add_foreign_key "forum_threads", "boards"
  add_foreign_key "forum_threads", "users", column: "created_by_id"
  add_foreign_key "forum_threads", "users", column: "updated_by_id"
  add_foreign_key "posts", "forum_threads", column: "thread_id"
  add_foreign_key "posts", "users", column: "created_by_id"
  add_foreign_key "posts", "users", column: "updated_by_id"
end
