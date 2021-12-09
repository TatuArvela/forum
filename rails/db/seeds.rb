# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the bin/rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

User.create!(id: 1, username: 'admin', email: '', password: 'admin', password_confirmation: 'admin', admin: true)
User.create!(id: 2, username: 'user', email: '', password: 'user', password_confirmation: 'user')

Board.create!(id: 1, title: 'Rails', description: 'Sample board',
              created_at: '2020-03-28T20:54:56.161Z', updated_at: '2020-03-28T20:54:56.161Z',
              created_by_id: 1, updated_by_id: 1)

ForumThread.create!(id: 1, board_id: 1, title: 'Development with Rails',
               created_at: '2020-03-28T20:55:13.546Z', updated_at: '2020-03-28T20:55:13.546Z',
               created_by_id: 1, updated_by_id: 1)

Post.create!(id: 1, message: 'Sample thread', thread_id: 1,
             created_at: '2020-03-28T20:55:13.547Z', updated_at: '2020-03-28T20:55:13.547Z',
             created_by_id: 1, updated_by_id: 1)
