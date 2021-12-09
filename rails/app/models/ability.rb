# frozen_string_literal: true

class Ability
  include CanCan::Ability

  def initialize(user)
    can :read, Post
    can :read, Thread
    can :read, Board

    return unless user.present?
    can :create, Post
    can :edit, Post, created_by: user

    can :create, Thread
    can :edit, Thread, created_by: user

    return unless user.admin?
    can :edit, Post
    can :destroy, Post

    can :edit, Thread
    can :destroy, Thread

    can :create, Board
    can :edit, Board
    can :destroy, Board

    can :create, User
    can :edit, User
    can :destroy, User
  end
end
