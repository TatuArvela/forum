Rails.application.routes.draw do
  root to: redirect('/boards/', status: 302)

  resources :boards, only: %i[index show new delete]

  resources :threads, only: %i[show delete]
  get '/threads/new/:id', to: 'threads#new'

  resources :posts, only: %i[show delete]
  get '/posts/new/:id', to: 'posts#new'
end
