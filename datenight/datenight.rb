#!/usr/bin/env ruby

$dates = nil

class DateIdeas

  def initialize()
    @date_ideas = []
  end

  def date(name, &block)
    date = DateIdea.new(name)
    date.instance_eval(&block)
    @date_ideas << date
  end

  def to_s
    str = "Date ideas:\n"
    @date_ideas.each do |f|
      str << "  #{f.to_s}"
    end
    str
  end

  def choose
    incomplete = @date_ideas.reject { |idea| !idea.complete? }
    num_dates = incomplete.length
    incomplete[rand(num_dates)]
  end

  def self.plan(&block)
    $dates = DateIdeas.new
    $dates.instance_eval(&block)
  end

end

class DateIdea

  ATTRIBUTES = %w(adventure romantic athletic intellectual)

  def initialize(name = "")
    @name = name.to_s
    @attributes = {}
    @requires = {}
    @outcome = nil
  end

  def kind(args)
    args.each do |field, value|
      @attributes[field] = value
    end
  end
  
  def requires(args)
    args.each do |field, value|
      @requires[field] = value
    end
  end
  
  def outcome(score)
    @outcome = score
  end

  def complete?
    @outcome == nil
  end

  def to_s
    attr_str = @attributes.map { |k,v|
      "#{k}: #{v}"
    }.join(", ")
    date_str = "#{@name}: (#{attr_str})"
    date_str = date_str + ", outcome: #{@outcome}" unless @outcome == nil
    "#{date_str}\n"
  end

end

infile = ARGV[0]
require infile

if ARGV.length == 1
  puts $dates.choose
else
  command = ARGV[1]
  
  if command == 'list'
    puts $dates
  else
    puts "Usage: ./datenight.rb <ideas-file> [list]"
  end
end
